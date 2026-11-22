// Run from a checkout, with DSH_RUNTIME pointing to a local npm install prefix.
import assert from 'node:assert/strict'
import { spawnSync } from 'node:child_process'
import { mkdirSync, mkdtempSync, readFileSync, realpathSync, rmSync } from 'node:fs'
import { createRequire } from 'node:module'
import { tmpdir } from 'node:os'
import { dirname, isAbsolute, join, resolve } from 'node:path'
import { pathToFileURL } from 'node:url'

const plugin = 'dsh-plugin-cells-alive'
const skill = 'cells-alive'
const providerId = 'skill-cells-alive'
const profile = 'cells-alive-evaluation'
const runtime = process.env.DSH_RUNTIME
const spec = process.env.DSH_PLUGIN_SPEC
assert.ok(runtime, 'Set DSH_RUNTIME to the npm prefix containing @deepseek-ai/dsh')
assert.ok(
  spec && ((isAbsolute(spec) && spec.endsWith('.tgz')) || /^github:[\w.-]+\/[\w.-]+#[0-9a-f]{40}$/i.test(spec)),
  'Set DSH_PLUGIN_SPEC to an absolute .tgz or github:owner/repo#<full-commit-sha>'
)

const fromPrefix = createRequire(join(resolve(runtime), 'package.json'))
const hostManifest = fromPrefix.resolve('@deepseek-ai/dsh/package.json')
const fromHost = createRequire(hostManifest)
const host = JSON.parse(readFileSync(hostManifest, 'utf8'))
const bin = join(dirname(hostManifest), host.bin.dsh)

const initialDirectory = process.cwd()
const parent = realpathSync(process.env.DSH_E2E_PARENT || tmpdir())
const work = mkdtempSync(join(parent, 'dsh-cells-alive-'))
const home = join(work, 'home')
const workspace = join(work, 'workspace')
mkdirSync(workspace)
process.env.DSH_HOME = home
process.env.DSH_TELEMETRY_DISABLED = '1'
process.env.CI = 'true'
process.chdir(workspace)

function command(executable, args, expected = 0) {
  const result = spawnSync(executable, args, {
    cwd: workspace,
    encoding: 'utf8',
    windowsHide: true,
    timeout: 180_000,
    maxBuffer: 16 * 1024 * 1024,
  })
  if (result.error) throw result.error
  assert.equal(result.status, expected, `${executable} exited with ${result.status}\n${result.stdout}\n${result.stderr}`)
  return result.stdout
}

let shutdown
let passed = false
try {
  command(process.execPath, [bin, 'plugin', '--profile', profile, 'add', spec])
  const profileDir = join(home, 'profiles', profile)
  const installed = JSON.parse(readFileSync(join(profileDir, 'package.json'), 'utf8'))
  assert.ok(installed.dsh.profile.bundles.includes(plugin))
  const dump = command(process.execPath, [bin, '--profile', profile, '--dump-config'])
  assert.ok(dump.includes(plugin) && dump.includes(providerId))

  const { runProfile } = await import(pathToFileURL(fromHost.resolve('@deepseek-ai/dsh/profile-boot')))
  const { loadLayeredEnv } = await import(pathToFileURL(fromHost.resolve('@deepseek-ai/dsh-app-boot')))
  const boot = await runProfile({ environment: loadLayeredEnv('dsh'), profile, patchFiles: [], args: [] })
  shutdown = boot.shutdown

  const options = { cwd: workspace }
  const listed = (await boot.ctx.skills.list(options)).find((item) => item.name === skill)
  assert.ok(listed, 'Expected cells-alive skill to be listed by DSH host')
  assert.equal(listed.provider, skill)
  assert.equal(listed.source, 'bundled')
  assert.ok(listed.invocation.modelInvocable && listed.invocation.userInvocable)

  const definition = await boot.ctx.skills.get(skill, options)
  assert.equal(definition.resourceBase.kind, 'directory')
  const base = realpathSync(definition.resourceBase.path)
  const packageRoot = realpathSync(join(profileDir, 'node_modules', plugin))
  assert.equal(base, realpathSync(join(packageRoot, 'skills', skill)))
  assert.equal(realpathSync(definition.path), realpathSync(join(base, 'SKILL.md')))
  assert.equal(/^---\r?\n/.test(definition.content), false, 'Stripped SKILL.md content must not start with YAML frontmatter')
  assert.ok(definition.content.includes('细胞还活着吗'))

  console.log(`DSH_HOST=PASS version=${host.version} provider=${listed.provider} source=${listed.source}`)
  passed = true
} finally {
  if (shutdown) await shutdown.shutdown(passed ? 0 : 1)
  process.chdir(initialDirectory)
  if (passed && !process.env.DSH_E2E_PARENT && dirname(realpathSync(work)) === parent) {
    rmSync(work, { recursive: true, force: true, maxRetries: 5, retryDelay: 200 })
  } else {
    console.log(`DSH_E2E_WORK=${work}`)
  }
}
console.log('DSH_E2E=PASS install, profile boot, skill list/get, resourceBase verified')
