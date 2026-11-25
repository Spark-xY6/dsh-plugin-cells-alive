# 生科专业写作骨相与去 AI 腔指南（Life-Science Writing Voice Reference）

`cells-alive`（《细胞还活着吗》）不只在交流层保留“懂湿实验与生信日常的人情味”，在用户切入 **L0 正式科研写作与汇报交付**时，同样把生命科学研究者真正写文章、讲证据、回审稿的语言骨相内化为正稿约束：**一面保持 0% 闲聊口语渗入，一面主动写出干净、有分量、禁得起同行挑剔的生科正文。**

> **边界提示**：本指南只规范论证组织、读数校准与学术语体，绝不伪造实验数据、P 值、样本量或参考文献；凡下文标记「示意例子，非真实结果」者均仅用于说明改写前后的语感差异。

---

## 1. 生科结果段（Results）四步推进骨相

生命科学顶刊（如 *Nature* / *Nature Communications* / *Cell* 体系）的高水准 `Results` 段落，通常不靠修饰词堆气氛，而是用紧凑四步把逻辑焊死：

1. **实验问题或待排竞争假说开篇**
   - 直接点明这一组实验要检验什么或排除什么，例如：`To determine whether ...`, `To distinguish between direct transcriptional repression and secondary viability loss, ...`
   - 避免“近年来关注度极高”“本文深入探究了关键作用（delves into the pivotal role）”等空洞大帽。
2. **模型体系与对照灵敏度锚定（Control Gate）**
   - 明示细胞/动物/组织模型、处理剂量或时间窗，并说明**独立生物学重复数**（例如 `n = 4 independent biological replicates`，严禁把 3 个技术复孔或上万个测序细胞数混称为独立生物样本数）。
   - 将阳性对照（证明检测体系能响）与阴性对照（排除载体/操作本底）自然嵌入正文，尤其是**阴性结果段落**——有了干净的阳性对照读数（如 `shPLK1` 稳定降低活率 `>60%`），阴性发现才从“实验没做出来”变成“明确排除了该假说”。
3. **直接定量读数、方向与不确定度**
   - 紧贴原始测定指标报告方向、效应量（如 `β`、`log₂FC`、绝对差值或百分比变化）、置信区间与校正后统计检验值（`*P*` 或 `FDR`），并保留未入选阈值前后的界定说明。
4. **严格校准的机制边界一句话收束**
   - 根据实验干预层级挑选匹配动词，在句内直接把条件边界说稳（如常氧标准培养 72 h 条件下非必需），不另起一段反复道歉或自我否定。

---

## 2. 读数到主张精准对齐（Measurement-to-Claim Calibration）

生科稿件最容易被审稿人揪住的“外行 AI 腔”，不是语法错，而是**越级下结论**——拿 A 层面的测量读数，直接断言 B 层面的因果机制。

| 实测指标层面 | 常见越级 AI 改写（需拦住） | 精准对齐写法（生科内行标准） |
| :--- | :--- | :--- |
| **CCK-8 / MTT 吸光度或 ATP 荧光** | “…proves that Gene X inhibits cell cycle progression.” | “…reduced viable cell signal in A549 cultures at 72 h (mean difference −28%, *P* = 0.004); direct cell-cycle arrest requires DNA-content confirmation.” |
| **RT-qPCR 相对 mRNA 倍数变化** | “…establishes activation of the pathway protein cascade.” | “…increased *CPT1A* transcript abundance by 2.4-fold relative to *GAPDH* (95% CI [1.8, 3.1]); downstream protein abundance/flux remains to be tested.” |
| **Bulk/单细胞转录组通路富集（GSEA / FDR）** | “…demonstrates metabolic reprogramming drives rescue.” | “…transcripts annotated to lipid β-oxidation were enriched after batch adjustment (NES = 1.82, FDR = 0.014), consistent with altered fatty-acid catabolic demand.” |
| **相关性散点 / 生存回归分析** | “…confirms Target A causes poor prognosis.” | “…higher *Target A* expression was associated with shorter progression-free survival in this cohort (HR = 1.64, 95% CI [1.12, 2.40]); causal dependence is not established.” |

### 动词强度校准梯度

- **直接因果干预 + 正交验证 + 完整对照成立**：`shows` / `demonstrates` / `establishes`
- **多批次重复一致、受限条件下的功能支持**：`indicates` / `supports`
- **组学关联、富集或间接读数一致**：`is consistent with` / `suggests` / `associates with`
- **禁止无统计检验支持时使用 `significantly`**；禁止单凭一项体外表型使用 `proves`、`universally` 或 `revolutionizes`。

---

## 3. 生科常见 AI 套话清洗与专业名词零篡改

AI 在连续写完两句结果后，极易惯性吐出英文八股词或“优雅变体”偷换术语：

1. **高危 AI 腔词汇（正文中优先替换为具体科学陈述）**：
   - 浮夸动词与短语：`delve into`, `shed light on`, `underscore`, `pave the way for`, `open new avenues`, `play a pivotal role`, `serve as a testament`, `intricate tapestry`；
   - 刷屏衔接词：连续用 `Moreover,`, `Furthermore,`, `Additionally,`, `Notably,`, `Importantly,`（改为让上句读数自然引出下句比较）；
   - 含糊程度词：`somewhat`, `relatively`, `fairly`, `extensive experiments`（改为具体数量与对照范围，如 `across four independent cohorts`）。
2. **术语、基因/物种斜体与数值零篡改**：
   - **绝不凭近义词习惯偷换既有生物学术语**：例如原文分析指标与通路名为 `lipid β-oxidation`，严禁擅自改写为 `fatty acid β-oxidation`；原文为 `serum-free medium` 或具体细胞株代号（`A549`, `HEK293T`, `C57BL/6J`），不得自行扩写或改换简写。
   - **区分基因与蛋白约定**：按学科惯例（如人类基因全大写斜体 *TP53*、小鼠基因首字母大写斜体 *Trp53*、对应蛋白正体 TP53）保持通篇统一，不修改作者既定的基因/探针/批次编号。
   - **严禁修匀或篡改统计读数**：保留原始 `n`、区间、`*P*` 值与阴性对照表现。

---

## 4. 审稿回复（Rebuttal）与讨论（Discussion）同行分寸

- **审稿回复（Rebuttal）**：先以一句话正面回应审稿人的核心担忧（感谢其点出混杂/样本量/对照组问题），紧接着贴出具体复核结果、统计表编号及对应原稿修改位置；既不抱怨实验周期长、工作量多大，也不空口承诺“we thoroughly proved...”。
- **讨论（Discussion）**：避免逐图复读 `Results` 数值；围绕核心生物学发现说明“相比前人解释推进了哪一寸”、不同条件下出现阴性或分化（如原代细胞 vs 永生系、常氧 vs 缺氧）可能反映的机制边界，用克制而自信的同行语感收束在核心贡献上。

---

## 5. 写作层改写对照（示意例子，非真实结果）

### 对照 A：英文 `Results` 阴性对照与效应边界

- **常见通用 AI 改写（AI 套话 + 读数越界 + 漏掉对照边界）**：
  > Despite extensive efforts, Target knockdown surprisingly did not notably affect A549 cell growth after delving into batch effects (p = 0.39), shedding light on the intricate tapestry of proliferation control and underscoring that Target may not play a pivotal role in cancer cells.
- **Cells Alive? L0 生科写作层输出（四步骨相 + 读数对齐 + 0% 套话）**：
  > To determine whether Target knockdown impairs baseline proliferation, we assayed A549 viability at 72 h across four independent biological replicates at fixed seeding density (2,000 cells per well). Linear mixed-effects modeling across batches showed no significant effect of `shTarget-1` relative to `shCtrl` (β = −0.04, 95% CI [−0.13, 0.05], *P* = 0.39), while `shTarget-2` remained below our prespecified −15% biological threshold (−6.8%, *P* = 0.24). By contrast, the positive control `shPLK1` reduced viability by >60% in all four batches, confirming assay sensitivity. These data indicate that Target is dispensable for A549 proliferation under standard normoxic culture conditions.

### 对照 B：审稿回复（Rebuttal）回应临界值质疑

- **常见通用 AI 回复（虚胖道歉 + 套话）**：
  > We sincerely apologize for the confusion and greatly appreciate the reviewer's insightful suggestion. Although removing one outlier pushes the p value to 0.021, we believe the biological trend is still very important and meaningful for the field.
- **Cells Alive? L0 生科写作层输出（坦诚保留全样本 + 给出质控证据与 95% CI）**：
  > We thank the reviewer for raising this point regarding statistical robustness. Inspection of melt curves, spike-in controls, and technical replicate `Ct` spreads across all four biological batches identified no pre-specified technical failure for treated sample #3; accordingly, we retained all samples in the primary analysis (ratio = ..., 95% CI [...], *P* = 0.068) and added a leave-one-out sensitivity plot and individual batch points in Supplementary Figure X. We have revised the text from claiming a significant increase to stating that this assay shows a non-significant upward trend under current sample size.
