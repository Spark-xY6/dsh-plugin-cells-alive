# 细胞还活着吗 · Cells Alive? (`dsh-plugin-cells-alive`)

[English](README.en.md) · [免安装离线体验页](adapters/start.html) · [配对实测记录](docs/comparison-and-showcase.md) · [共创征集](community/README.md)

<img src="./icon.svg" width="64" height="64" alt="Cells Alive? 图标"/>

*先问细胞，再问问你自己还活着吗。科学是服务于人的——先把做实验的人照顾好。*

专为湿实验与生信人写的轻量同行规则（仅 **6 行 / `< 2 KB`**）：懂阳性对照、批次效应与统计红线，卡壳时不甩千字说教清单，切回写英文论文与代码时 **0% 口语渗入**。

![生科实验与组学配对实测：批次退展不催清单、p = 0.068 守红线、Results 英文零渗入](docs/images/cells-alive-showcase.png)

## 什么时候最适合叫上它

- **实验阴性或加严校正“退展”时**：三批原代 `rescue` 阴性或重跑 `DESeq2` 后 `FDR > 0.38` 时，先认准你已经做扎实的对照与复核，缓过来只给 **1 个生科小抓手**（如对比效应量或查最近端靶标），不套话“抱抱”、不当心理咨询师。
- **组会前夜纠结删点，或赶考核要算账时**：四批 `qPCR` 卡在 `p = 0.068` 坚决拦住按 `p` 值踢 3 号样本，先查熔解曲线与复孔 `Ct` 并直接附好组会全样本汇报原话；读可选 `.cells-alive.yaml` 兼容硕博 / 博后 / PI 身份（PI 止损模式省约 **19.7%** 冗余篇幅），平静问数时零多余寒暄。
- **深夜收工存断点，接着改英文正稿时**：一句话收稳今晚进度提醒休息，转身改写 `Nature Comms` 英文 `Results` 时完全静默退场，完整守住 `lipid β-oxidation` 等专业词不被改歪。

## 怎么用（免安装网页或插件任选）

| 你平时在哪用 AI | 30 秒直接上手 |
| --- | --- |
| **网页端 ChatGPT / Claude / DeepSeek** | 双击打开纯离线 [adapters/start.html](adapters/start.html)（含「**深夜台灯**」暗色模式），选一条实验室场景点「复制到聊天」即可，本机还带断点便签。 |
| **DeepSeek Harness (DSH)** | 运行 `dsh plugin --profile web add (Resolve-Path '.\dsh-plugin-cells-alive-0.3.0.tgz').Path` 后重启，零依赖。 |
| **Codex / Claude Code / Cursor** | 直接复用 [AGENTS 片段](adapters/agents-md-snippet.md)、[Cursor 规则](adapters/cursor-rule.mdc) 或 [.claude-plugin/plugin.json](.claude-plugin/plugin.json)。 |

<details>
<summary>常用实验室开场白示例（点开即复制）</summary>

- “加严 `~ batch + condition` 和 FDR 后差异全平（`FDR > 0.38`），前面两周是不是白干了？帮我查是批次混杂还是效能不足。”
- “qPCR 做了四批卡在 `p = 0.068`，踢掉 3 号孔变 `0.021`。帮我核孔位质控并写一段明天组会原话。”
- “凌晨 `01:40` 刚把 `.rds` 存好断点；把这段肝细胞 `lipid beta-oxidation` 结果改写进 `Results` 英文正文。”

</details>

**Zhuocheng Yao** ([@Spark-xY6](https://github.com/Spark-xY6)) & **Xuehua Zhao** ([@snowflakee685-commits](https://github.com/snowflakee685-commits)) 共同参与设计（社会工作非评判性共情视角）。非临床医疗工具，绝不纵容删点或 p-hacking。[共创墙](community/README.md) · [MIT License](LICENSE)
