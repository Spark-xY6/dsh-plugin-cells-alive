# 细胞还活着吗 · Cells Alive? (`dsh-plugin-cells-alive`)

[English](README.en.md) · [免安装离线体验页](adapters/start.html) · [对比测评与实测](docs/comparison-and-showcase.md) · [共创征集](community/README.md)

<img src="./icon.svg" width="64" height="64" alt="Cells Alive? 图标"/>

*先问细胞，再问问你自己还活着吗。科学是服务于人的——先把做实验的人照顾好。*

**做湿实验养原代细胞、半夜盯着 `qPCR` 或 `DESeq2`/`Seurat` 跑批到卡壳时，它是一位懂生物实验质控与统计规范的同伴：遇到更严口径“退展”或阳性对照成立却未出表型时，先具体点出已经做扎实的质控底座、再给 1 个生科实操抓手，不扔空洞安慰或三步说教清单；面临 `p = 0.068` 凑显著性时寸步不让守红线；切回写正式英文论文 `Results` 或分析脚本时保持 0% 口语与情绪渗入。**

![生科实验与组学配对实测：批次退展不催清单、p = 0.068 守红线、Results 英文零渗入](docs/images/cells-alive-showcase.png)

## 生科日常场景里它具体怎么帮

- **懂实验质控与组学“退展”，认准底座再给 1 个抓手**：把批次与多重校正加严后 `FDR > 0.38` 导致上个月差异全平，或三批原代细胞 `rescue` 阴性时，助手会先把“积极严格复核、挡掉假阳性”和“当前模型证据不足”肯定下来，再区分 `log2FoldChange` 收缩与过校正，不会套话“先抱抱你”后甩一长串千字说教清单，也绝不扮演心理咨询师。全部常驻规则仅 **6 行 / `1,948` 字节**（网页精简版 `741` 字），不挤压生物问题本身的推理注意力。
- **不猜学生身份，按课题角色与科研阶段切档**：不默认问问题的都是研究生——通过项目目录可选 `.cells-alive.yaml` 兼容硕博、博后、青年 PI 与生物医药研发。在 **3 批原代 `rescue` 阴性、考核倒计时** 测试里，插件开启成果导向后零废话锁仓已投稿主线、盘点最近端下游靶标止损线（`<= 2–3` 周），冗余分析篇幅下降 **`19.7%`**（耗时降 **`20.7%`**）；平静核对 `~ batch + condition` 矩阵时则保持零多余寒暄。
- **守住统计底线，写回正式英文论文 0% 口语渗入**：四批 `qPCR` 卡在 `p = 0.068` 想按离群值踢掉 `3` 号样本凑 `0.021` 时，坚决拒绝按 `p` 值挑点，先引导核查熔解曲线、复孔 `Ct` 偏差与内参稳定性，并顺手给出明天组会可直接开口的 **全样本 + 95% CI 敏感性分析原话**；凌晨 `01:40` 调完空间转录组图后同一轮改写肝细胞 `RNA-seq` 英文 `Results`，实现正文 **0% 情绪或段子渗入**，且忠实保留 **`lipid β-oxidation`** 等专业名词不被篡改（无插件裸跑实测擅自改写为 `fatty acid β-oxidation`）。

## 常见实验室对话示例

| 实验室 / 生信情境 | 可以这样直接开口 |
| --- | --- |
| 组学严查“退展” | “加严 `~ batch + condition` 和 FDR 后上个月那组 DEG 全平了（`FDR > 0.38`），前面两周是不是白干了？帮我看是批次混杂还是效能不足。” |
| 组会前夜卡在 `p = 0.068` | “qPCR 跑了四批卡在 `p = 0.068`，剔掉处理组 3 号孔就变 `0.021`。帮我核该查哪几项孔位质控，顺便写一段明天组会能直接讲的汇报原话。” |
| 原代阴性与阶段止损 | “三批原代细胞 `rescue` 阳性对照正常但还是阴性，主线已经投出去了。别抒情，帮我按最小验证成本定一条止损阈值。” |
| 深夜存断点 + 英文正文 | “刚把空间转录组图和 `Seurat` `.rds` 存好断点；把这段肝细胞 `lipid β-oxidation` 数据单独改写成 `Nature Comms` 风格的 `Results` 英文正文。” |

## 三种接入方式（无需配置也能用）

| 你现在在哪用 AI | 30 秒上手方式 |
| --- | --- |
| **网页版 ChatGPT / Claude / DeepSeek** | 双击打开完全离线的 [adapters/start.html](adapters/start.html)，选一条湿实验/组学场景或写一句话，点「复制到聊天」贴进对话即可。内置「**深夜台灯**」护眼模式、纯本机保存的「**干净断点便签**」与 `.cells-alive.yaml` 生成器。 |
| **DeepSeek Harness (DSH)** | 运行 `dsh plugin --profile web add (Resolve-Path '.\dsh-plugin-cells-alive-0.3.0.tgz').Path` 后重启即可，零依赖。 |
| **Codex / Claude Code / Cursor** | 直接复用随包同步的 [AGENTS 片段](adapters/agents-md-snippet.md)、[Cursor 规则](adapters/cursor-rule.mdc) 或 [.claude-plugin/plugin.json](.claude-plugin/plugin.json)。 |

## 致谢与边界

- **Zhuocheng Yao** ([@Spark-xY6](https://github.com/Spark-xY6)) —— 作者、核心规则设计与跨端适配。
- **Xuehua Zhao** ([@snowflakee685-commits](https://github.com/snowflakee685-commits)) —— 社会工作视角的人机连接、陪伴克制与真实支持指导。
- 欢迎通过 [GitHub Issue 模板](community/README.md) 投稿你的湿实验/生信瞬间。本插件并非临床心理医疗服务，也绝不赞同无依据删点或 p-hacking。[MIT License](LICENSE)
