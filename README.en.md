# Cells Alive? · Warm Research Companion for Life Sciences (`dsh-plugin-cells-alive`)

[简体中文](README.md) · English · [Offline Starter](adapters/start.html) · [Landscape & Eval](docs/comparison-and-showcase.md) · [Community](community/README.md)

<img src="./icon.svg" width="64" height="64" alt="Cells Alive?"/>

*First check the cells. Then check on you. Warm, lab-savvy human feel in daily research chat—so talking to AI feels grounded instead of draining.*

A **5-line (`< 2 KB`)** research companion focused squarely on **human-centered interaction in wet-lab and bioinformatics workflows**: plenty of tools already polish English grammar or wrap scripts, so this plugin focuses on speaking real lab shop talk without 3-step lecture checklists, adapting across career stages, defending statistical rigor, and stepping aside silently (**0% casual leakage**) when you switch to formal writing or code.

![Warm midnight bench companion dialogue showcase](./docs/images/cells-alive-showcase.png)

## Why the interaction feel clicks

- **Speaks lab reality without therapy scripts**: When `~ batch + condition` pushes `DESeq2` hits to `FDR > 0.38` or 3 primary-cell `rescue` batches fail despite clean controls, it credits the QC already banked and offers **1 low-burden check**—no `"hug you"` clichés or long todo dumps.
- **Role-aware pacing & calm-data silence**: Optional `.cells-alive.yaml` adapts cleanly across grad students, postdocs, PIs, and R&D (`outcome_driven` PI mode trims **19.7%** redundant text); routine matrix/QC checks run with **0%** filler chatter.
- **Kind tone with a scientific spine**: Refuses `p`-hacking at `p = 0.068` (`0.021`), checks melt curves/replicate `Ct` first, drafts honest lab-meeting wording, and stays strictly isolated (**0% casual leakage**, terms intact) whenever you move to formal manuscripts or dedicated writing plugins.

## How to use (try offline in 30 seconds, or install as a plugin)

| Where you work | 30-second setup |
| --- | --- |
| **Web ChatGPT / Claude / DeepSeek** | Open [adapters/start.html](adapters/start.html) offline (warm oat paper + **Night lamp** mode + local **Clean Breakpoint** note), pick a lab scenario, and copy. |
| **DeepSeek Harness (DSH)** | Run `dsh plugin --profile web add (Resolve-Path '.\dsh-plugin-cells-alive-0.3.0.tgz').Path` and restart. |
| **Codex / Claude Code / Cursor** | Copy [adapters/agents-md-snippet.md](adapters/agents-md-snippet.md), [adapters/cursor-rule.mdc](adapters/cursor-rule.mdc), or [.claude-plugin/plugin.json](.claude-plugin/plugin.json). |

<details>
<summary>Quick lab prompts to try</summary>

- “Re-running DESeq2 with `~ batch + condition` pushed all my hits to `FDR > 0.38`. Did I waste two weeks, or is batch confounding masking the signal?”
- “Four qPCR batches sit at `p = 0.068`; dropping treated sample #3 makes `0.021`. Which melt-curve/Ct checks matter, and what can I say tomorrow?”
- “Saved my Seurat `.rds` checkpoint at `01:40`—wrapping up now; help me note one minimal check for tomorrow morning.”

</details>

Created by **Zhuocheng Yao** ([@Spark-xY6](https://github.com/Spark-xY6)) with social-work guidance from **Xuehua Zhao** ([@snowflakee685-commits](https://github.com/snowflakee685-commits)). Not clinical therapy; never endorses dropping outliers or p-hacking. [Contribute](community/README.md) · [MIT License](LICENSE)
