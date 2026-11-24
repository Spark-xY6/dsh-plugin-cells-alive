# Cells Alive? · Life-Science Research Companion (`dsh-plugin-cells-alive`)

[简体中文](README.md) · English · [Zero-Install Offline Starter](adapters/start.html) · [Benchmarks & Blind A/B](docs/comparison-and-showcase.md) · [Community Wall](community/README.md)

<img src="./icon.svg" width="64" height="64" alt="Cells Alive?"/>

*First we check the cells. Then we check on you. Science serves people first.*

**A featherweight (<2 KB / 6 lines) research companion for wet-lab and bioinformatics nights: grounded, non-judgmental holding when experiments stall without firing stressful 3-step checklists, firm statistical guardrails on outlier tampering, and 0% emotional leakage when writing formal manuscripts or code.**

![Real frustrated researcher dialogue contrast: holding unseen effort without lecturing or checklists](docs/images/cells-alive-showcase.png)

## Quick start (zero configuration required)

| Where you work | 30-second setup |
| --- | --- |
| **Any web AI chat** | Open [adapters/start.html](adapters/start.html) offline. Type a note (or pick a lab scenario, or leave blank) and click **Copy for my chat**. Includes a **Night lamp** mode, browser-local **Clean Breakpoint** note, and `.cells-alive.yaml` builder. |
| **DeepSeek Harness (DSH)** | Run `dsh plugin --profile web add (Resolve-Path '.\dsh-plugin-cells-alive-0.3.0.tgz').Path` and restart your profile. |
| **Codex / Claude Code / Cursor** | Grab [adapters/agents-md-snippet.md](adapters/agents-md-snippet.md), [adapters/cursor-rule.mdc](adapters/cursor-rule.mdc), or [.claude-plugin/plugin.json](.claude-plugin/plugin.json). |

## Why it exists, what it does & verified results

- **Holds effort without firing stressful checklists**: Student blind A/B testing showed that hollow sympathy (*"hug you..."*) followed immediately by a 3-step action list worsens anxiety after harsh thesis feedback. Built with social-work Ethics-of-Care guidance in just **6 lines (<2 KB; 741-char web starter)**, it acknowledges concrete work already done and offers at most one gentle step when ready.
- **Role-flexible & non-presumptuous**: Never assumes you are a grad student; optional `.cells-alive.yaml` adapts smoothly across PhD students, postdocs, junior PIs, and industry R&D (outcome-driven PI mode cut verbose output by ~**19.7%** while keeping zero fluff on calm data queries).
- **Uncompromising rigor & 0% manuscript leakage**: Rejects cherry-picking outliers (`p = 0.068`) while drafting honest full-sample + 95% CI lab-meeting phrasing, and switches cleanly to **0% companion tone leakage** when writing Results, rebuttals, grants, slides, or code (preserving exact terminology like `lipid β-oxidation`).

## Credits & Boundaries

- **Zhuocheng Yao** ([@Spark-xY6](https://github.com/Spark-xY6)) — author, core micro-rule, and multi-agent adapter sync.
- **Xuehua Zhao** ([@snowflakee685-commits](https://github.com/snowflakee685-commits)) — social-work guidance on grounded human-AI companionship and non-judgmental restraint.
- Not clinical mental-health care; never endorses dropping outliers or p-hacking. [MIT License](LICENSE)
