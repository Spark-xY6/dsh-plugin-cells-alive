# Cells Alive? · Life-Science Research Companion (`dsh-plugin-cells-alive`)

[简体中文](README.md) · English · [Zero-Install Offline Starter](adapters/start.html) · [Paired Eval](docs/comparison-and-showcase.md) · [Community Wall](community/README.md)

<img src="./icon.svg" width="64" height="64" alt="Cells Alive?"/>

*First check the cells. Then check on you. Science serves people first.*

A featherweight **6-line (`< 2 KB`)** research companion built for wet-lab benches and bioinformatics clusters: it understands positive controls, batch correction, and statistical red lines, skips hollow 3-step lecture checklists, and enforces **0% casual leakage** inside formal English `Results` and code.

![Paired life-science evaluation showcase: batch/FDR setback holding, p = 0.068 guardrail, and 0% Results leakage](docs/images/cells-alive-showcase.png)

## When to reach for it

- **Negative primary-cell assays or flattened DEG re-runs**: When stricter `~ batch + condition` re-runs push hits to `FDR > 0.38` or 3 primary-cell `rescue` batches fail despite clean controls, it recognizes the QC already banked and offers **1 low-burden scientific step** (`log2FoldChange` vs `lfcSE`) instead of `"hug you"` scripts or therapy talk.
- **Pre-lab-meeting `p = 0.068` temptations & milestone triage**: Blocks `p`-driven dropping of sample #3 (`0.021`), checks melt curves / replicate `Ct` first, and drafts clean full-sample + 95% CI wording. Adapts across PhD students, postdocs, and PIs via optional `.cells-alive.yaml` (PI mode trims **19.7%** redundant text; calm data queries get zero fluff).
- **Midnight checkpoints before switching back to manuscript prose**: Wraps up a `01:40` spatial transcriptomics run in 2 grounded lines, then goes completely silent in formal `Nature Comms` `Results`—preserving exact terms like `lipid β-oxidation`.

## How to use (no install required, or add as plugin)

| Where you work | 30-second setup |
| --- | --- |
| **Web ChatGPT / Claude / DeepSeek** | Open [adapters/start.html](adapters/start.html) offline (includes **Night lamp** dark mode & local **Clean Breakpoint** note), pick a lab chip, and click **Copy for my chat**. |
| **DeepSeek Harness (DSH)** | Run `dsh plugin --profile web add (Resolve-Path '.\dsh-plugin-cells-alive-0.3.0.tgz').Path` and restart. |
| **Codex / Claude Code / Cursor** | Copy [adapters/agents-md-snippet.md](adapters/agents-md-snippet.md), [adapters/cursor-rule.mdc](adapters/cursor-rule.mdc), or [.claude-plugin/plugin.json](.claude-plugin/plugin.json). |

<details>
<summary>Quick lab prompts to try</summary>

- “Re-running DESeq2 with `~ batch + condition` pushed all my hits to `FDR > 0.38`. Did I waste two weeks, or is batch confounding masking the signal?”
- “Four qPCR batches sit at `p = 0.068`; dropping treated sample #3 makes `0.021`. Which melt-curve/Ct checks matter, and what can I say tomorrow?”
- “Saved my Seurat `.rds` checkpoint at `01:40`. Rewrite this hepatocyte `lipid beta-oxidation` finding into clean `Results` prose.”

</details>

Created by **Zhuocheng Yao** ([@Spark-xY6](https://github.com/Spark-xY6)) with social-work guidance from **Xuehua Zhao** ([@snowflakee685-commits](https://github.com/snowflakee685-commits)). Not clinical therapy; never endorses dropping outliers or p-hacking. [Contribute](community/README.md) · [MIT License](LICENSE)
