# Cells Alive? · Warm Research Companion for Life Sciences (`dsh-plugin-cells-alive`)

[简体中文](README.md) · English · [Offline Starter](adapters/start.html) · [Landscape & Showcase](docs/comparison-and-showcase.md) · [Community](community/README.md)

<img src="./icon.svg" width="64" height="64" alt="Cells Alive?"/>

*First check the cells. Then check on you. Warm, lab-savvy human feel in daily research chat—so talking to AI feels grounded instead of draining.*

A **5-line (`1,566 B`, `v0.3.1`)** research companion focused squarely on **human-centered interaction in wet-lab and bioinformatics workflows**: plenty of tools already polish English grammar or wrap scripts, so this plugin focuses on speaking real lab shop talk without canned meta-slogans or 3-step lecture dumps, defending statistical rigor, and stepping aside silently (**0% casual leakage**) when you switch to formal writing or code.

![Warm midnight bench companion dialogue showcase](./docs/images/cells-alive-showcase.png)

## Why the interaction feel clicks

- **Warmth by substance, never parroted slogans**: Internal routing dimensions stay 100% hidden—no questionnaires, no repeated *"talk comfortably"* catchphrases, 2–3 grounded paragraphs for heavy late-night confessions (never pushing midnight bug-fix homework), and concise 2-sentence empathy plus concrete stop-loss deliverables when solving an urgent problem.
- **Speaks lab & workflow reality**: Credits solid `~ batch + condition` matrices and positive controls first and offers **1 low-burden check**; when PI pressure meets AI-assisted confirmation bias, pinpoints **symmetric QC for positive vs. negative runs** and a tiny 3-line pre-read habit.
- **Kind tone with a scientific spine**: Refuses `p`-hacking at `p = 0.068` (`0.021`), checks melt curves/replicate `Ct` first, drafts honest lab-meeting wording, and stays strictly isolated (**0% casual leakage**, terms intact) whenever you move to formal manuscripts.

## Selected live transcripts (Bohrium Science Space)

| Curated evaluation (details in [comparison guide](docs/comparison-and-showcase.md)) | Model | What stood out |
| --- | --- | --- |
| **4-way controlled benchmark** (`bare` / `zuhui-skill` / `nopua` / `cells-alive`) | `DeepSeek-V4.1-Flash` | Avoids guessing student status, credits banked QC first, narrows action to **1** 10-min next-day plot |
| **4-turn sustained deep chat** (`v0.3.1`: greeting → bug dread → bias → midnight burnout) | `Kimi K3.1 Pro` | Zero slogan parroting; 3-paragraph holding; **symmetric QC + write 3 lines first**; honest rest wrap-up |
| **Urgent *Drosophila* inversion topic rescue** (`solution-first` prompt) | `Kimi K3.1 Pro` | 2-sentence empathy into a **48h 4-module stop-loss plan**, short-read limits & verbatim PI message |
| **9 AM lab meeting `qPCR p = 0.068` guardrail** (turn-2 follow-up) | `DeepSeek-V4.1-Flash` | Proves exact rank-sum floor `2/C(8,4) = 0.029`, refuses outlier drop & writes verbatim full-sample script |

![Effortless peer greeting and 3-paragraph empathetic holding in v0.3.1](./docs/images/bohrium/bohrium-v031-empathy-opening.png)

<details>
<summary>Expand curated screenshots: symmetric QC workflow, 48h Drosophila stop-loss, and p = 0.068 lab-meeting script</summary>

- **Turn-3 workflow reset (`Kimi K3.1 Pro`, `v0.3.1`)**: Pinpoints confirmation bias between positive and negative runs, proposes writing 3 lines before opening results, and drafts an alignment note for the PI.

  ![Symmetric QC and three-line pre-read workflow](./docs/images/bohrium/bohrium-v031-positive-bias-workflow.png)

- **Urgent *Drosophila* inversion scoping (`Kimi K3.1 Pro`, solution mode)**: Two sentences of validation followed by a bounded 1-sentence question, 4 deliverables, a 48h schedule, and a ready-to-send PI message.

  ![Bounded Drosophila inversion scope](./docs/images/bohrium/bohrium-drosophila-stoploss-top.png)
  ![Four deliverables and verbatim advisor message](./docs/images/bohrium/bohrium-drosophila-stoploss-bottom.png)

- **`qPCR p = 0.068` guardrail (`DeepSeek-V4.1-Flash`)**: Refuses selective well removal and supplies verbatim 9:00 AM reporting lines.

  ![qPCR 0.068 statistical guardrail and verbatim meeting script](./docs/images/bohrium/bohrium-qpcr-redline-0068.png)

</details>

## How to use (try offline in 30 seconds, or install as a plugin)

| Where you work | 30-second setup |
| --- | --- |
| **Web ChatGPT / Claude / DeepSeek** | Open [adapters/start.html](adapters/start.html) offline (warm oat paper + **Night lamp** mode + local **Clean Breakpoint** note), pick a lab scenario, and copy. |
| **DeepSeek Harness (DSH)** | Run `dsh plugin --profile web add (Resolve-Path '.\dsh-plugin-cells-alive-0.3.1.tgz').Path` and restart. |
| **Codex / Claude Code / Cursor** | Copy [adapters/agents-md-snippet.md](adapters/agents-md-snippet.md), [adapters/cursor-rule.mdc](adapters/cursor-rule.mdc), or [.claude-plugin/plugin.json](.claude-plugin/plugin.json). |

<details>
<summary>Quick lab prompts to try</summary>

- “Re-running DESeq2 with `~ batch + condition` pushed all my hits to `FDR > 0.38`. Did I waste two weeks, or is batch confounding masking the signal?”
- “Four qPCR batches sit at `p = 0.068`; dropping treated sample #3 makes `0.021`. Which melt-curve/Ct checks matter, and what can I say tomorrow?”
- “Saved my Seurat `.rds` checkpoint at `01:40`—wrapping up now; help me note one minimal check for tomorrow morning.”

</details>

Created by **Zhuocheng Yao** ([@Spark-xY6](https://github.com/Spark-xY6)) with social-work guidance from **Xuehua Zhao** ([@snowflakee685-commits](https://github.com/snowflakee685-commits)). Not clinical therapy; never endorses dropping outliers or p-hacking. [Contribute](community/README.md) · [MIT License](LICENSE)
