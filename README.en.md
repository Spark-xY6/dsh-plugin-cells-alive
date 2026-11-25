# Cells Alive? · Life-Science Research Companion (`dsh-plugin-cells-alive`)

[简体中文](README.md) · English · [Offline Starter](adapters/start.html) · [Landscape & Eval](docs/comparison-and-showcase.md) · [Bio Writing Voice](skills/cells-alive/references/bio-writing-voice.md) · [Community](community/README.md)

<img src="./icon.svg" width="64" height="64" alt="Cells Alive?"/>

*First check the cells. Then check on you. Warm peer chat when benches stall; authentic life-science prose when writing.*

A **6-line (`< 2 KB`)** research companion built for wet-lab benches and bioinformatics clusters: speaks real lab shop talk without 3-step lecture checklists, guards statistical red lines, and switches cleanly to **0% casual leakage** with authentic **life-science writing craft** inside formal `Results` and `Rebuttal` drafts.

![Dual-layer showcase: lab-savvy peer holding, p = 0.068 guardrail, and life-science Results prose](./docs/images/cells-alive-showcase.png)

## Why the two-layer split clicks

- **Warm, lab-savvy interaction layer**: When `~ batch + condition` pushes `DESeq2` hits to `FDR > 0.38` or 3 primary-cell `rescue` batches fail despite clean controls, it banks the QC already achieved and offers **1 low-burden check**—no `"hug you"` scripts or therapy talk. Refuses `p`-hacking at `p = 0.068` (`0.021`), checks melt curves/replicate `Ct` first, and drafts clean lab-meeting wording. Optional `.cells-alive.yaml` adapts across PhD students, postdocs, PIs, and R&D (PI mode trims **19.7%** redundant text).
- **Authentic life-science writing layer (`L0`, 0% leakage)**: After saving a `01:40` `.rds` checkpoint, formal English `Results`, `Methods`, and `Rebuttal` text enforces **question -> control sensitivity gate -> quantitative readout (`n`, CI) -> bounded inference**, calibrates claims strictly to what the assay measured, strips AI clichés (`delve`, `pivotal`, `shed light on`), and preserves exact terms like `lipid β-oxidation`.

## How to use (no install required, or add as plugin)

| Where you work | 30-second setup |
| --- | --- |
| **Web ChatGPT / Claude / DeepSeek** | Open [adapters/start.html](adapters/start.html) offline (**Night lamp** dark mode + local **Clean Breakpoint** note), pick a lab scenario, and copy. |
| **DeepSeek Harness (DSH)** | Run `dsh plugin --profile web add (Resolve-Path '.\dsh-plugin-cells-alive-0.3.0.tgz').Path` and restart. |
| **Codex / Claude Code / Cursor** | Copy [adapters/agents-md-snippet.md](adapters/agents-md-snippet.md), [adapters/cursor-rule.mdc](adapters/cursor-rule.mdc), or [.claude-plugin/plugin.json](.claude-plugin/plugin.json). |

<details>
<summary>Quick lab prompts to try</summary>

- “Re-running DESeq2 with `~ batch + condition` pushed all my hits to `FDR > 0.38`. Did I waste two weeks, or is batch confounding masking the signal?”
- “Four qPCR batches sit at `p = 0.068`; dropping treated sample #3 makes `0.021`. Which melt-curve/Ct checks matter, and what can I say tomorrow?”
- “Saved my Seurat `.rds` checkpoint at `01:40`. Rewrite this hepatocyte `lipid beta-oxidation` finding into clean `Results` prose.”

</details>

Created by **Zhuocheng Yao** ([@Spark-xY6](https://github.com/Spark-xY6)) with social-work guidance from **Xuehua Zhao** ([@snowflakee685-commits](https://github.com/snowflakee685-commits)). Not clinical therapy; never endorses dropping outliers or p-hacking. [Contribute](community/README.md) · [MIT License](LICENSE)
