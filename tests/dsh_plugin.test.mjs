import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');

test('DSH cordis plugin contract & bundle manifests', async () => {
  const pkgRaw = await fs.readFile(path.join(ROOT, 'package.json'), 'utf8');
  const pkg = JSON.parse(pkgRaw);
  assert.equal(pkg.name, 'dsh-plugin-cells-alive');
  assert.equal(pkg.dsh?.bundle?.patch, './cordis.patch.yml');
  assert.ok(pkg.engines?.dsh, 'engines.dsh should be declared');
  assert.equal(pkg.dependencies ?? undefined, undefined, 'Zero runtime npm dependencies expected');

  const iconStat = await fs.stat(path.join(ROOT, pkg.icon));
  assert.ok(iconStat.isFile(), 'package.json icon file must exist');

  const patchText = await fs.readFile(path.join(ROOT, 'cordis.patch.yml'), 'utf8');
  assert.match(patchText, /^-\s*insert:/m, 'cordis.patch.yml must use - insert: syntax');
  assert.match(patchText, /id:\s*skill-cells-alive/);
  assert.match(patchText, /name:\s*['"]dsh-plugin-cells-alive['"]/);

  for (const [locFile, expectedDetail] of [
    ['zh-CN.json', 'README.zh.md'],
    ['en-US.json', 'README.md'],
  ]) {
    const loc = JSON.parse(await fs.readFile(path.join(ROOT, 'locale', locFile), 'utf8'));
    assert.equal(loc.meta?.detail, expectedDetail);
    const readmeRaw = await fs.readFile(path.join(ROOT, expectedDetail), 'utf8');
    assert.equal(readmeRaw.charCodeAt(0) === 0xfeff, false, `${expectedDetail} must not contain UTF-8 BOM`);
    assert.equal(/^---\r?\n/.test(readmeRaw), false, `${expectedDetail} must not begin with YAML frontmatter`);
  }

  const mod = await import(new URL('../lib/index.js', import.meta.url).href);
  assert.equal('default' in mod, false, 'Function plugin must not export default');
  assert.equal(mod.name, 'skill-cells-alive');
  assert.deepEqual(mod.inject, ['skills']);
  assert.equal(typeof mod.apply, 'function');

  const registered = [];
  const mockCtx = {
    skills: {
      registerProvider(factory) {
        registered.push(factory());
        return () => {};
      },
    },
  };
  mod.apply(mockCtx);
  assert.equal(registered.length, 1);

  const provider = registered[0];
  const candidates = await provider.list();
  assert.equal(candidates.length, 1);
  const cand = candidates[0];
  assert.equal(cand.name, 'cells-alive');
  assert.match(cand.name, /^[a-z0-9]+(?:-[a-z0-9]+)*$/);
  assert.ok(cand.description.length > 10 && cand.description.length <= 500);
  assert.equal(cand.rank, 600);
  assert.equal(cand.source, 'bundled');
  assert.equal(cand.invocation.modelInvocable, true);
  assert.equal(cand.invocation.userInvocable, true);
  assert.equal(cand.resourceBase?.kind, 'directory');

  const stat = await fs.stat(cand.path);
  assert.ok(stat.isFile());

  const def = await provider.get(cand);
  assert.equal(def.name, 'cells-alive');
  assert.equal(/^---\r?\n/.test(def.content), false, 'get() must return stripped markdown body');
  assert.ok(def.content.includes('细胞还活着吗'));
});
