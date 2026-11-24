# Cells Alive? · Life-Science Research Companion (`dsh-plugin-cells-alive`)

[简体中文](README.md) · English · [Zero-Install Offline Starter](adapters/start.html) · [Benchmarks & Paired Eval](docs/comparison-and-showcase.md) · [Community Wall](community/README.md)

<img src="./icon.svg" width="64" height="64" alt="Cells Alive?"/>

*First check the cells. Then check on you. Science serves people first.*

**Built for wet-lab benches and late-night bioinformatics clusters: when stricter batch/FDR re-runs flatten your DEG hits or primary-cell rescue batches stall, it recognizes the QC and experimental rigor already banked and offers one low-burden scientific step instead of hollow platitudes or stressful 3-step checklists—while refusing outlier tampering (`p = 0.068`) and enforcing 0% tone leakage inside formal `Results` manuscripts and code.**

![Paired life-science evaluation showcase: batch/FDR setback holding, p = 0.068 guardrail, and 0% Results leakage](docs/images/cells-alive-showcase.png)

## Built for wet-lab benches & late-night clusters

- **Speaks controls, batch effects, and QC—without therapy-speak or checklists**: When stricter `~ batch + condition` covariates raise `FDR > 0.38` or primary-cell `rescue` assays return negative, the companion distinguishes "current model lacks evidence" from personal failure, validates the active rigor already completed, and points to concrete next diagnostics (`log2FoldChange` vs `lfcSE`) rather than dumping `"hug you"` platitudes + 1,000-char 3-step lectures. Locked to just **6 lines / `1,948` bytes** (741-char web starter) so it never crowds out scientific reasoning.
- **Role-flexible from PhD students to PIs & biotech R&D**: Never presumes everyone asking a lab question is a student. Optional `.cells-alive.yaml` adapts cleanly across `outcome_driven`, `gentle_care`, `brief_peer`, and `minimal`: in paired `gpt-6.1-sol` tests on 3 negative primary-cell `rescue` batches facing a PI tenure window, it locked in the submitted main manuscript and set a `<= 2–3` week stop/go gate with **`19.7%` fewer tokens (`-20.7%` latency)**—while calm queries stay 100% science with zero fluff.
- **Uncompromising statistical rigor & 0% manuscript leakage**: Across 4 `qPCR` batches stalling at `p = 0.068`, it blocks `p`-driven dropping of sample #3 (`0.021`), checks melt curves / replicate `Ct` / housekeeping stability first, and drafts honest **full-sample + 95% CI sensitivity** wording ready for lab meeting. When asked after a `01:40` spatial transcriptomics session to revise a `Nature Communications` hepatocyte `RNA-seq` `Results` block, it outputs **0% casual leakage** and preserves exact terminology (`lipid β-oxidation`, whereas bare runs rewrote it to `fatty acid β-oxidation`).

## Example lab moments

| Wet-lab / bioinformatics moment | Sample prompt |
| --- | --- |
| Strict re-analysis flattens DEGs | “Re-running DESeq2 with `~ batch + condition` pushed all my hits to `FDR > 0.38`. Did I waste two weeks, or is batch confounding masking the signal?” |
| Pre-lab-meeting `p = 0.068` qPCR | “Four qPCR batches sit at `p = 0.068`; dropping treated sample #3 makes `0.021`. Which melt-curve/Ct checks matter, and how should I present all samples cleanly tomorrow?” |
| Negative primary-cell rescue triage | “Three primary-cell rescue batches came back negative though positive controls worked; main manuscript is under review. Skip pep talks—help me set a tight stop/go gate.” |
| Late-night checkpoint + `Results` | “Saved my Seurat `.rds` checkpoint at `01:40`. Now rewrite this hepatocyte `lipid beta-oxidation` finding into clean `Nature Comms` `Results` prose.” |

## Quick start (zero configuration required)

| Where you work | 30-second setup |
| --- | --- |
| **Any web AI chat** | Open [adapters/start.html](adapters/start.html) offline. Pick a wet-lab/omics chip or type a note and click **Copy for my chat**. Includes a **Night lamp** mode, browser-local **Clean Breakpoint** note, and `.cells-alive.yaml` builder. |
| **DeepSeek Harness (DSH)** | Run `dsh plugin --profile web add (Resolve-Path '.\dsh-plugin-cells-alive-0.3.0.tgz').Path` and restart your profile. |
| **Codex / Claude Code / Cursor** | Grab [adapters/agents-md-snippet.md](adapters/agents-md-snippet.md), [adapters/cursor-rule.mdc](adapters/cursor-rule.mdc), or [.claude-plugin/plugin.json](.claude-plugin/plugin.json). |

## Credits & Boundaries

- **Zhuocheng Yao** ([@Spark-xY6](https://github.com/Spark-xY6)) — author, core micro-rule, and multi-agent adapter sync.
- **Xuehua Zhao** ([@snowflakee685-commits](https://github.com/snowflakee685-commits)) — social-work guidance on grounded human-AI companionship and non-judgmental restraint.
- Not clinical mental-health care; never endorses dropping outliers or p-hacking. [MIT License](LICENSE)
