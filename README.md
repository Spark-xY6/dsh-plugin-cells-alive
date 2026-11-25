# 细胞还活着吗 · Cells Alive? (`dsh-plugin-cells-alive`)

[English](README.en.md) · [免安装离线体验页](adapters/start.html) · [行业对照与配对实测](docs/comparison-and-showcase.md) · [生科写作骨相](skills/cells-alive/references/bio-writing-voice.md) · [共创征集](community/README.md)

<img src="./icon.svg" width="64" height="64" alt="Cells Alive? 图标"/>

*先问细胞，再问问你自己还活着吗。科学是服务于人的——交流有人情味，写稿有生科味。*

专为湿实验与生信人写的 **6 行 / `< 2 KB`** 科研同行规则：日常对话懂对照、批次与复孔消耗、卡壳不甩千字清单；切写 `Results` / `Rebuttal` 时 **0% 口语渗入**，按生科论证骨相把读数对齐主张并剔除 AI 套话。

![交流层人情味、统计红线与生科写作骨相实测](./docs/images/cells-alive-showcase.png)

## 两层各管各的事，才顺手

- **交流层（有人情味，懂生科常识）**：三批原代 `rescue` 阴性或重跑 `DESeq2` 后 `FDR > 0.38` 时，先认准你做稳的对照与复核，缓过来只给 **1 个生科抓手**，不当心理咨询师；四批 `qPCR` 卡在 `p = 0.068` 绝不顺从按 `p` 值删点，先查熔解曲线与复孔 `Ct` 并直接配好全样本 + `95% CI` 组会原话；可选 `.cells-alive.yaml` 兼容硕博 / 博后 / PI / 研发（PI 止损模式输出省约 **19.7%**），平静问数零寒暄。
- **写作层（纯正生科骨相，0% 口语渗入）**：凌晨收工存好 `.rds` 断点，转身写英文 `Results` 或审稿回复时情感完全静默退场，直接按**问题 -> 对照灵敏度锚定 -> 独立重复与定量读数 -> 证据边界**组织段落，守住读数到主张对齐、`lipid β-oxidation` 等术语不篡改，洗掉 `delve` / `pivotal` / `shed light on` 等 AI 八股词。

## 怎么用（免安装网页或插件任选）

| 你平时在哪用 AI | 30 秒直接上手 |
| --- | --- |
| **网页端 ChatGPT / Claude / DeepSeek** | 双击打开纯离线 [adapters/start.html](adapters/start.html)（含「**深夜台灯**」暗色模式与「**干净断点便签**」），点一条实验室场景即可复制到聊天。 |
| **DeepSeek Harness (DSH)** | 运行 `dsh plugin --profile web add (Resolve-Path '.\dsh-plugin-cells-alive-0.3.0.tgz').Path` 后重启，零依赖。 |
| **Codex / Claude Code / Cursor** | 直接复用 [AGENTS 片段](adapters/agents-md-snippet.md)、[Cursor 规则](adapters/cursor-rule.mdc) 或 [.claude-plugin/plugin.json](.claude-plugin/plugin.json)。 |

<details>
<summary>常用实验室开场白示例（点开即复制）</summary>

- “加严 `~ batch + condition` 和 FDR 后差异全平（`FDR > 0.38`），前面两周是不是白干了？帮我查是批次混杂还是效能不足。”
- “qPCR 做了四批卡在 `p = 0.068`，踢掉 3 号孔变 `0.021`。帮我核孔位质控并写一段明天组会原话。”
- “凌晨 `01:40` 刚把 `.rds` 存好断点；把这段肝细胞 `lipid beta-oxidation` 结果按生科 `Results` 风格改写进英文正文。”

</details>

**Zhuocheng Yao** ([@Spark-xY6](https://github.com/Spark-xY6)) & **Xuehua Zhao** ([@snowflakee685-commits](https://github.com/snowflakee685-commits)) 共同参与设计（社会工作非评判性共情视角）。非临床医疗工具，绝不纵容删点或 p-hacking。[共创墙](community/README.md) · [MIT License](LICENSE)
