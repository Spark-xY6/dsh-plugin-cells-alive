/**
 * DeepSeek Harness Cordis plugin provider for the bundled `cells-alive` skill.
 * Zero runtime dependencies: registers directly against `ctx.skills`.
 *
 * @module dsh-plugin-cells-alive
 */

import { readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';

const PROVIDER_NAME = 'cells-alive';
const BUNDLED_SKILL_RANK = 600;
const SKILL_DIR = fileURLToPath(new URL('../skills/cells-alive/', import.meta.url));
const SKILL_MD_URL = new URL('../skills/cells-alive/SKILL.md', import.meta.url);
const SKILL_MD_PATH = fileURLToPath(SKILL_MD_URL);
const RESOURCE_BASE = Object.freeze({ kind: 'directory', path: SKILL_DIR });

function parseBoolFlag(raw, fallback) {
  if (raw === undefined) return fallback;
  const v = raw.trim().toLowerCase();
  if (v === 'true' || v === 'yes' || v === 'on' || v === '1') return true;
  if (v === 'false' || v === 'no' || v === 'off' || v === '0') return false;
  return fallback;
}

function parseSkillMarkdown(raw) {
  const m = /^---\r?\n([\s\S]*?)\r?\n---(?:\r?\n|$)/u.exec(raw);
  if (!m || m[1] === undefined) {
    throw new Error('dsh-plugin-cells-alive: SKILL.md is missing YAML frontmatter');
  }
  const fields = {};
  const lines = m[1].split(/\r?\n/u);
  let i = 0;
  while (i < lines.length) {
    const line = lines[i] ?? '';
    if (!line.trim() || line.startsWith(' ') || line.startsWith('#')) {
      i += 1;
      continue;
    }
    const idx = line.indexOf(':');
    if (idx <= 0) {
      i += 1;
      continue;
    }
    const key = line.slice(0, idx).trim();
    let val = line.slice(idx + 1).trim();
    if (val === '>-' || val === '>' || val === '|' || val === '|-') {
      const blockLines = [];
      i += 1;
      while (i < lines.length) {
        const nextLine = lines[i] ?? '';
        if (!nextLine.trim() || nextLine.startsWith(' ')) {
          if (nextLine.trim()) blockLines.push(nextLine.trim());
          i += 1;
        } else {
          break;
        }
      }
      fields[key] = blockLines.join(val.startsWith('|') ? '\n' : ' ');
      continue;
    }
    if ((val.startsWith('"') && val.endsWith('"')) || (val.startsWith("'") && val.endsWith("'"))) {
      val = val.slice(1, -1);
    }
    fields[key] = val;
    i += 1;
  }
  const skillName = fields.name || PROVIDER_NAME;
  const description = fields.description || '';
  if (!description) {
    throw new Error('dsh-plugin-cells-alive: SKILL.md frontmatter requires description');
  }
  const disableModel = parseBoolFlag(fields['disable-model-invocation'], false);
  const userInvocable = parseBoolFlag(fields['user-invocable'], true);
  return {
    name: skillName,
    description,
    whenToUse: fields.whenToUse,
    modelInvocable: !disableModel,
    userInvocable,
    content: raw.slice(m[0].length).trim(),
  };
}

const provider = {
  name: PROVIDER_NAME,
  async list() {
    const raw = await readFile(SKILL_MD_URL, 'utf8');
    const parsed = parseSkillMarkdown(raw);
    return [
      {
        name: parsed.name,
        description: parsed.description,
        ...(parsed.whenToUse ? { whenToUse: parsed.whenToUse } : {}),
        invocation: {
          modelInvocable: parsed.modelInvocable,
          userInvocable: parsed.userInvocable,
        },
        provider: PROVIDER_NAME,
        source: 'bundled',
        resourceBase: RESOURCE_BASE,
        path: SKILL_MD_PATH,
        rank: BUNDLED_SKILL_RANK,
        locator: SKILL_MD_URL,
      },
    ];
  },
  async get() {
    const raw = await readFile(SKILL_MD_URL, 'utf8');
    const parsed = parseSkillMarkdown(raw);
    return {
      name: parsed.name,
      description: parsed.description,
      ...(parsed.whenToUse ? { whenToUse: parsed.whenToUse } : {}),
      invocation: {
        modelInvocable: parsed.modelInvocable,
        userInvocable: parsed.userInvocable,
      },
      provider: PROVIDER_NAME,
      source: 'bundled',
      resourceBase: RESOURCE_BASE,
      path: SKILL_MD_PATH,
      content: parsed.content,
    };
  },
};

export const name = 'skill-cells-alive';
export const inject = ['skills'];

export function apply(ctx) {
  ctx.skills.registerProvider(() => provider);
}
