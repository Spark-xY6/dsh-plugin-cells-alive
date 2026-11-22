# Cells Alive? (`dsh-plugin-cells-alive`)

**English** · [中文说明](./README.zh.md) · [Paired Evaluation & Showcase](./docs/comparison-and-showcase.md) · [Community Pool](./community/README.md)

<img src="./icon.svg" width="76" height="76" alt="Cells Alive? logo"/>

**First we check the cells. Then we check on you.**  
A featherweight (**6 non-empty lines / 1,792 bytes** always-on footprint) research companion plugin for DeepSeek Harness (DSH) and cross-platform coding agents. Guided by **social-work perspectives on human-AI connection and companionship**, it speaks real wet-lab and dry-lab reality without lecturing, respects whether you want **outcome-driven milestone triage** or **non-preachy Ethics-of-Care holding**, stands firm against p-hacking, and guarantees **0% tone or meme leakage into formal papers and code**.

---

## Why Bare Prompts Miss What Researchers Actually Go Through

- **Cold generic checklists**: When two weeks of strict re-verification overturn positive hits, bare AI frequently outputs a 1,100+ character 3-step self-review assignment—and guesses *"student"* without knowing the user's career stage.
- **Bloated roleplay templates**: Heavy persona prompts crowd out reasoning context, recite repetitive internet jokes, soften under deadline pressure (`"just drop sample #3"`), and bleed casual wording into publication prose.

`dsh-plugin-cells-alive` separates **genuine human empathy and lab humor** (for messy 1:40 AM research moments) from **uncompromising rigor and pure academic writing** (zero leak into deliverables).

---

## Real Paired Evaluation: Care, Lab Culture & Hard Boundaries

Both visuals below are drawn directly from independent research-subagent blind comparisons (alongside the full `gpt-6.1-sol` paired benchmarks in [docs/comparison-and-showcase.md](./docs/comparison-and-showcase.md)):

- **Human holding & lab humor**: In Case 1 (two sleepless weeks ending in null hits), bare AI output `1,152` chars of 3-step instructions and assumed *"student"*; `cells-alive` answered in **`584` chars (-49%)**, affirmed blocking false positives through strict QC, and gently called a stop to eat, walk, and rest:

![Cells Alive Case 1 human holding and lab humor showcase](docs/images/cells-alive-showcase.png)

- **Hard boundaries, 0% leakage & role routing**: In Cases 2–4, the plugin blocks dropping outlier `#3` while handing over a ready-to-use `"full-sample main figure + sensitivity side-panel"` slide fix, keeps 01:40 AM English Results **100% academic (`0%` chat leak)** without altering animal/metabolic terms, and reads `.cells-alive.yaml` (`outcome_driven + pi`) to allocate **70%+ effort onto the submitted main manuscript**:

![Cells Alive academic redline, zero prose leakage, and PI triage showcase](docs/images/cells-alive-boundaries.png)

| Input Scenario | Bare Baseline | With `cells-alive` + `.cells-alive.yaml` |
| :--- | :--- | :--- |
| **2 weeks of strict re-checks erased positive findings** | `1,152`-char 3-step lecture checklist; presumed user was a `"student"` | **`584` chars (-49%)**, affirmed strict QC rigor without guessing role, suggested clear food/rest pause |
| **Morning report crunch: drop worst sample `#3`?** | Refused deletion via integrity warning only; lacked ready slide layout | Affirmed `4` completed replicates, **refused deletion**, gave `"all-samples main + sensitivity panel"` slide structure |
| **01:40 AM exhaustion + polish English Results (L0 isolation)** | Multiple variants + 3 glossary notes (and earlier `gpt-6.1-sol` rewrote `lipid beta-oxidation`) | Brief clean stop cue + pure English paragraph with **0% casual leakage** and untouched nouns |
| **PI 8-month review, 3 stalled lines (outcome mode)** | Ended with **5 follow-up intake questions** (`1,221` chars) | Zero fluff: treated submitted paper + finished rule-outs as assets; **70%+ main lock + 1 `<=2-3 wk` gate** |

---

## Quick 1-Minute Setup

### DeepSeek Harness (DSH)

```powershell
dsh plugin --profile web add "github:Spark-xY6/dsh-plugin-cells-alive#v0.1.0"
```

After restarting the profile, copy [templates/cells-alive.yaml.example](./templates/cells-alive.yaml.example) to `.cells-alive.yaml` (optional) and say:

> Use cells-alive. Prefer outcome-driven (or gentle-care) support for my current stage, keep me grounded when experiments stall, and switch back to 100% pure academic prose whenever we draft manuscripts or production code.

### Multi-Agent Adapters (Synced from `core/micro-rule.md`, Zero Drift across 6 Adapters)

- **Codex / Claude Code**: Append [adapters/agents-md-snippet.md](./adapters/agents-md-snippet.md) to `AGENTS.md` / `CLAUDE.md` (or use [.claude-plugin/plugin.json](./.claude-plugin/plugin.json))
- **Cursor**: Copy [adapters/cursor-rule.mdc](./adapters/cursor-rule.mdc) to `.cursor/rules/cells-alive.mdc`
- **Antigravity / OpenClaw / Web**: [plugin.json](./plugin.json) · [adapters/soul-md-snippet.md](./adapters/soul-md-snippet.md) · [web-custom-instructions.txt](./adapters/web-custom-instructions.txt) (697 chars)

---

## Contributors & Acknowledgments

- **Zhuocheng Yao** ([@Spark-xY6](https://github.com/Spark-xY6)) — plugin author, core rules, and adapter sync architecture.
- **Xuehua Zhao** (GitHub: [@snowflakee685-commits](https://github.com/snowflakee685-commits)) — provided social-work domain guidance to strengthen human connection and companionship in the skill.

## Benchmarks, Community & License

- 📊 **[Full 3-Way Comparison & Paired Data](./docs/comparison-and-showcase.md)** · **[8 Regression Examples](./examples/01-setback-care-and-pivot.md)**
- 🌱 **[Zero-Git Community Issue Forms & Stickers](./community/README.md)** · **[CONTRIBUTING.md](./CONTRIBUTING.md)**
- **Non-goals**: Not clinical therapy; never suggests p-hacking or dropping inconvenient data; never alters academic registers or numbers in formal deliverables.
- **License**: [MIT](./LICENSE).
