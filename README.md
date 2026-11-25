# 细胞还活着吗 · Cells Alive? (`dsh-plugin-cells-alive`)

[English](README.en.md) · [免安装离线体验页](adapters/start.html) · [行业对照与配对实测](docs/comparison-and-showcase.md) · [共创征集](community/README.md)

<img src="./icon.svg" width="64" height="64" alt="Cells Alive? 图标"/>

*先问细胞，再问问你自己还活着吗。把懂湿实验与组学日常的“好人味儿”还给科研 AI，让每天开口的真实体感更好。*

专为湿实验与生信人打磨的 **5 行 / `< 2 KB`** 同伴规则：市面上帮改语法、查脚本的工具已经很多，我们专注先把**“日常对话懂实验、有温度、不让人越聊越累”**做到顺手——听得懂对照、批次与复孔消耗，卡壳不甩千字清单，切回写正文或代码时 **0% 口语串味**。

![深夜实验台边的同门回音：先认准功夫、再轻递抓手的温和对话界面](./docs/images/cells-alive-showcase.png)

## 把“好人味儿”做成不越界的日常体感

- **懂实验脉络，不当心理咨询师**：重跑 `DESeq2` 后 `FDR > 0.38` 或三批原代 `rescue` 阴性时，先认准你做稳的对照与批次功夫；不说“抱抱你”或“你不矫情”，缓过来只递 **1 个最小生科抓手**。
- **看人看场景调档，平静问数 0% 废话**：可选 `.cells-alive.yaml` 兼容硕博 / 博后 / 青年 PI / 企业研发（青年 PI 止损模式实测输出精简 **19.7%**、耗时降 **20.7%**）；正常核查设计矩阵时直切数据、零多余寒暄。
- **温柔有脊梁，且正稿 0% 串味**：四批 `qPCR` 卡在 `p = 0.068` 绝不顺从按 `p` 值删点，先查熔解曲线与复孔 `Ct` 并直接配好全样本 + `95% CI` 组会汇报原话；切回写论文正稿或代码时陪伴语气安静退场（术语数值零篡改），可随时搭配你惯用的专职写作插件。

## 怎么用（推荐先打开纯离线体验网页，或直接挂进客户端）

| 你平时在哪用 AI | 30 秒直接上手 |
| --- | --- |
| **网页端 ChatGPT / Claude / DeepSeek** | 双击打开纯离线 [adapters/start.html](adapters/start.html)（暖燕麦纸感 +「**深夜台灯**」护眼模式 +「**干净断点便签**」），选一条场景即可复制到聊天。 |
| **DeepSeek Harness (DSH)** | 运行 `dsh plugin --profile web add (Resolve-Path '.\dsh-plugin-cells-alive-0.3.0.tgz').Path` 后重启，零依赖。 |
| **Codex / Claude Code / Cursor** | 直接复用 [AGENTS 片段](adapters/agents-md-snippet.md)、[Cursor 规则](adapters/cursor-rule.mdc) 或 [.claude-plugin/plugin.json](.claude-plugin/plugin.json)。 |

<details>
<summary>常用实验室开场白示例（点开即复制）</summary>

- “加严 `~ batch + condition` 和 FDR 后差异全平（`FDR > 0.38`），前面两周是不是白干了？帮我查是批次混杂还是效能不足。”
- “qPCR 做了四批卡在 `p = 0.068`，踢掉 3 号孔变 `0.021`。帮我核孔位质控并写一段明天组会原话。”
- “凌晨 `01:40` 刚把 `.rds` 存好断点，先收工；明天醒来我只需要比对这几个 top 基因效应量。”

</details>

**Zhuocheng Yao** ([@Spark-xY6](https://github.com/Spark-xY6)) & **Xuehua Zhao** ([@snowflakee685-commits](https://github.com/snowflakee685-commits)) 共同参与设计（社会工作非评判性共情视角）。非临床医疗工具，绝不纵容删点或 p-hacking。[共创墙](community/README.md) · [MIT License](LICENSE)
