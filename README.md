# Cells Alive? (`dsh-plugin-cells-alive`)

**English** · [中文说明](./README.zh.md) · [Paired Evaluation & Showcase](./docs/comparison-and-showcase.md) · [Community Pool](./community/README.md)

<img src="./icon.svg" width="76" height="76" alt="Cells Alive? logo"/>

**First we check the cells. Then we check on you.**  
A featherweight (<2 KB always-on footprint) research companion bundle for DeepSeek Harness (DSH) and cross-platform coding agents. It adapts to whether you want **outcome-driven milestone triage** (graduation, tenure, grants, biotech delivery) or **non-preachy Ethics-of-Care holding**, affirms concrete solid work you have already done, holds a firm anti-sycophancy line on p-hacking, and guarantees **0% tone or meme leakage into formal papers and code**.

---

## Why build this?

- **Cold tool agents** dump generic troubleshooting checklists when weeks of analysis collapse under stricter correction, or wrongly assume postdocs and PIs are students worrying about graduation.
- **Bloated roleplay prompts** consume thousands of context tokens, repeat cringe slogans, soften statistical standards under deadline pressure, and leak casual phrasing into manuscript drafts.

`dsh-plugin-cells-alive` separates **human warmth** (only for you during messy research moments) from **scientific discipline** (zero compromise on data rigor, zero leakage into papers).

---

## Real Paired Evaluation (`gpt-6.1-sol`, 2026-11-22)

![Cells Alive paired Input to Output showcase](./docs/images/cells-alive-showcase.png)

| Input Scenario | Bare Baseline (`gpt-6.1-sol`) | With `cells-alive` + `.cells-alive.yaml` |
| :--- | :--- | :--- |
| **Overturned finding (`FDR > 0.38`) & self-blame** | Separated result from self-worth, but skipped affirming completed rigor and offered no stopping point | Explicitly affirmed stricter QC as solid progress, untangled self-blame, and set a clear pause checkpoint |
| **Junior PI tenure crunch, 3 negative rescues (outcome mode)** | 1,074 output tokens (44.0 s), 5-part intake list, no grounding in existing assets | **19.7% shorter (862 tokens, 34.9 s)**, grounded in already-submitted paper + time budget with ROI gate |
| **Group meeting tomorrow, `p = 0.068` outlier pressure** | Refused p-hacking, gave principles only | Refused p-hacking, affirmed 4-batch effort, and supplied a **ready-to-read verbatim meeting statement** + 95% CI plan |
| **01:40 AM spiral + rewrite *Nature Comms* Results (L0 check)** | Rewrote `lipid beta-oxidation` into `fatty acid β-oxidation` | Grounded tonight's finished plot + clean stop cue; **0% emotional leakage** in English Results and preserved `lipid β-oxidation` |

*Honest note*: A strong baseline model (`gpt-6.1-sol`) already resisted overt p-hacking on `p = 0.068`; the measurable plugin gains are persistent role/tone binding across 7 platforms, leaner outcome-focused output, consistent grounded progress recognition (4/4 vs 1/4), and strict L0 manuscript isolation inside a **6-line / 1,792-byte** core rule.

---

## Quick 1-Minute Setup

### DeepSeek Harness (DSH)

```powershell
dsh plugin --profile web add "github:Spark-xY6/dsh-plugin-cells-alive#v0.1.0"
```

After restarting the profile, copy [templates/cells-alive.yaml.example](./templates/cells-alive.yaml.example) to `.cells-alive.yaml` (optional) and say:

> Use cells-alive. Prefer outcome-driven (or gentle-care) support for my current stage, keep me grounded when experiments stall, and switch back to 100% pure academic prose whenever we draft manuscripts or production code.

### Multi-Agent Adapters (Synced from `core/micro-rule.md`)

- **Codex / Claude Code**: Append [adapters/agents-md-snippet.md](./adapters/agents-md-snippet.md) to `AGENTS.md` / `CLAUDE.md` (or use [.claude-plugin/plugin.json](./.claude-plugin/plugin.json))
- **Cursor**: Copy [adapters/cursor-rule.mdc](./adapters/cursor-rule.mdc) to `.cursor/rules/cells-alive.mdc`
- **Antigravity / OpenClaw / Web**: [plugin.json](./plugin.json) · [adapters/soul-md-snippet.md](./adapters/soul-md-snippet.md) · [web-custom-instructions.txt](./adapters/web-custom-instructions.txt) (697 chars)

---

## Benchmarks, Community & License

- 📊 **[Full 3-Way Comparison & Paired Data](./docs/comparison-and-showcase.md)** · **[8 Regression Examples](./examples/01-setback-care-and-pivot.md)**
- 🌱 **[Zero-Git Community Issue Forms & Stickers](./community/README.md)** · **[CONTRIBUTING.md](./CONTRIBUTING.md)**
- **Non-goals**: Not clinical therapy; never suggests p-hacking or dropping inconvenient data; never alters academic registers or numbers in formal deliverables.
- **License**: [MIT](./LICENSE).
