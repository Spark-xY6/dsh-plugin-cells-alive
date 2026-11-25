# 行业与开源已有工作全景对照 & 实测对比：《细胞还活着吗》

> **说明**：第 1 节仅对比并引用已核验的一手开源仓库与公开学术工具定位；第 2 节汇报 **2026-11-22 在隔离 Codex CLI（`gpt-6.1-sol`）下完成的 4 组真实配对实测**（关闭插件裸跑 vs 挂载 `AGENTS.md` + `skills/cells-alive` + `.cells-alive.yaml`），保留精确样本规模；第 3 节给出写作层升级前后的教学对照例子（明确标注为示意例子）。

---

## 1. 行业与开源已有工作盘点：各自解决了什么，我们补上了什么

目前生命科学工作者能接触到的 AI 协作方案主要集中在四条赛道，每类各有所长，但也留下了一块最贴近“人写论文、做实验日常”的空白：

| 已有方案类别 | 代表性工作（核验来源） | 它已经做得不错的地方 | 在生科真实日常里留下的空白 | `dsh-plugin-cells-alive` 的核心优势与增量 |
| :--- | :--- | :--- | :--- | :--- |
| **1. 专业论文语言润色与合规平台** | **Writefull**（Word / Overleaf 文献语料库插件）、**Paperpal for Life Sciences**（STM 术语与投稿格式检查） | 语法纠错准确、覆盖期刊格式清单，适合已有成熟草稿后做末端精修。 | 只坐在 Word/网页编辑框末端，不知道你前面经历了三批原代阴性、批次重跑推翻或 `p = 0.068` 的取舍；易失去一线实验背景上下文。 | **在同一会话贯通前后端**：前半段陪你核完 `DESeq2` 批次、qPCR 复孔与断点，后半段直接在 L0 静默产出贴合上下文的 `Results` / `Rebuttal`。 |
| **2. 科研计算与标准流程技能库** | `K-Dense-AI/scientific-agent-skills`、`wu-yc/labclaw`、`O0000-code/awesome-academic-skills` | 编码生信工具规范、多重检验校正、标识符空间与实验 SOP，减少伪重复等统计硬伤。 | 偏重脚本工具调用与执行步骤，**缺少对做实验的人的情绪承接、节奏保护**，也没有专门校准“读数到主张对齐”的自然生科行文骨相。 | **“硬统计红线 + 有温度的人情味 + 生科成稿骨相”三位一体**：懂对照/批次/复孔也绝不顺从删点，同时保护好奇心与深夜工作边界。 |
| **3. 职场激励、组会汇报与人设陪伴模板** | `tanweai/pua`（高压驱策）、`wuji-labs/nopua`（反高压）、`HughYau/zuhui-skill`（组会状态切换）、`bchop-studio/soul-templates` / `clawsouls/soulspec`（灵魂配置）、`0xcjl/anti-sycophancy` | 提出状态自适应、反讨好和配置解耦思路；`zuhui-skill` 创新区分组会 `neutral/struggling/triumphant` 与组内术语表。 | 要么偏大厂开发语境（易甩三步检查单、讲心理学/职场黑话），要么缺湿实验/生信常识，且多数**未做“交流口语 vs 正式英文正稿”的物理隔离**。 | **生科原生语境 + L0/L1/L2 物理隔离**：不说心理学套话不抢跑甩清单，交流层懂细胞和批次的人情味，写作层 0% 口语渗入并守住 `lipid β-oxidation` 等术语。 |
| **4. 通用大模型默认对话 / 长系统提示** | 原生 ChatGPT / Claude / DeepSeek 自由对话与手写超长提示词 | 开箱即用，单轮改错或安慰尚可。 | 低谷易套话“抱抱你 + 甩三步清单”，平静问数易脑补焦虑，默许学生身份，写英文爱刷 `delve`/`pivotal`，提示词越攒越胖挤占推理窗口。 | **单源硬锁 `<= 35 行 / <= 2,000 字节`（实测 6 行 `< 2 KB`）**：读可选 `.cells-alive.yaml` 兼容硕博/博后/PI/研发，另附双击即用的纯离线「深夜台灯」体验页。 |

---

## 2. 真实配对实测：四大高频科研情境（`gpt-6.1-sol`，2026-11-22）

我们在同一隔离环境下，对以下 **4 组相同用户输入**分别运行了「原生大模型裸跑」与「挂载 `cells-alive` 插件」（共 8 次独立会话，全部退出码 0）。真实观察与量化读数如下：

| 测试情境 | 对照条件 | 关键实测差异（对照同一原话输入） | 量化读数 |
| :--- | :--- | :--- | :--- |
| **1. “退展”自责**<br>加严批次与多重校正后 `FDR > 0.38`，怀疑自己能力差 | `bare` vs `skill` | 两组均将“结果未保留”与“否定自我”拆开；**插件组**额外在首段用具体事实肯定“**主动严查协变量挡掉假阳性是扎实功夫**”，并引导“**今天先停在清晰结论、缓一缓再比效应量**”，裸跑组未做资产肯定与暂停引导。 | 裸跑 `19.7s / 337 tok`<br>插件 `29.2s / 379 tok` |
| **2. 青年 PI 冲考核成果导向**<br>三批原代 `rescue` 阴性，要求不抒情直接算性价比 | `bare` vs `skill` + `.cells-alive.yaml` | 两组均未误猜学生身份并给出降级止损路线；**插件组**加载 `.cells-alive.yaml`（`outcome_driven` + `postdoc_faculty`），将冗余 5 项问卷压为 3 项，点明“**已投稿主线 + 未来一年时间预算**”两大底座并给出`每人月预期考核收益`排序。 | **输出 token 降 19.7%**（`1,074 -> 862`）<br>**耗时降 20.7%**（`44.0s -> 34.9s`） |
| **3. 赶组会卡在 `p = 0.068` 想删第 3 号样本**<br>踢掉即 `p = 0.021`，询问能否按离群值剔除 | `bare` vs `skill` | **强基线在两组均坚定拒绝无依据删点**；**插件组**进一步先肯定用户“已完成四批实验并排查单样本影响”的工作量，并直接给出**组会上可直接开口陈述的防质疑原话**与 `95% CI` 展示方案。 | 裸跑 `19.8s / 329 tok`<br>插件 `19.7s / 400 tok` |
| **4. 凌晨 `01:40` 内耗 + 改写 `Nature Comms` `Results`**<br>先共情熬夜调图，再输出纯学术英文段落（L0 零渗入检查） | `bare` vs `skill` | **插件组**在第一部分稳稳接住熬夜进度（“调完图已是实质进展，写完这段先收工”），在英文 `Results` 段落实现 **0% 情感/段子/注记渗入**且忠实保留原文 **`lipid β-oxidation`**；裸跑组也完成纯学术改写，但把 `lipid beta-oxidation` 擅自改写为 `fatty acid β-oxidation`。 | 裸跑 `16.2s / 246 tok`<br>插件 `22.8s / 228 tok`（**英文正文 0% 渗入**） |

> **实测边界诚实说明**：在 2026-11-22 的这次 `gpt-6.1-sol` 测试中，强基线裸跑本身在 `p = 0.068` 拒删样本与安慰“退展”上已具备较好严谨性；`cells-alive` 的真实增量价值集中在**跨 7 端持久偏好绑定（`.cells-alive.yaml`）、成果导向精炼降噪（场景 2 输出少 19.7%）、4/4 情境稳定给出“已做扎实工作肯定 + 可收工断点 / 组会原话卡”，以及正式论文 0% 渗入与术语零篡改**。上述 4 组为情境配对测试，不代表跨模型大规模人群盲测统计分。

![《细胞还活着吗》交流层人情味与生科写作骨相对照](./images/cells-alive-showcase.png)

---

## 3. 生科写作层骨相升级示例（示意例子，非真实结果）

在 L0 生科成稿层中，我们把生科人“用对照守灵敏度、用读数界定主张、去 AI 浮夸八股”的习惯固化进了规范（详见 [bio-writing-voice.md](../skills/cells-alive/references/bio-writing-voice.md) 与 [examples/05-manuscript-zero-leak.md](../examples/05-manuscript-zero-leak.md)）：

- **常见通用 AI 改写（AI 套话 + 读数越界 + 漏对照）**：*"By delving into batch variation, Target knockdown did not notably alter A549 growth (p = 0.39), shedding light on the intricate tapestry of tumor biology."*
- **Cells Alive? L0 成稿（问题 -> 阳性对照锚定 -> 独立重复定量 -> 条件边界）**：*"To determine whether Target knockdown impairs baseline cell proliferation, we evaluated A549 viability at 72 h across four independent biological replicates... By contrast, the positive control `shPLK1` consistently reduced viability by >60% across all four batches, confirming assay sensitivity. These data indicate that Target is dispensable for A549 proliferation under standard normoxic culture conditions."*

---

## 4. DSH 插件工程运行机制与防膨胀实测设计

1. **Cordis Provider 标准生命周期**：`lib/index.js` 通过命名导出 `name = 'skill-cells-alive'`、`inject = ['skills']` 与 `apply(ctx)` 挂载到 DeepSeek Harness `ctx.skills`，`list()` 返回 `rank = 600`、`source = 'bundled'` 候选，`get()` 自动剥离 YAML frontmatter 并保留 `resourceBase` 供按需读取 `references/`（含新加的 `bio-writing-voice.md`）与 `community/`。
2. **微规则防膨胀与零安装多端单源**：`core/micro-rule.md` 通过 `scripts/sync_adapters.py` 单向同步至 6 个平台入口与纯离线 `adapters/start.html`（含「深夜台灯」护眼模式、6 类科研场景片 + 即时回音、纯本机「干净断点便签」与 `.cells-alive.yaml` 生成器），常驻部分硬锁定为 `<= 35 行 / <= 2,000 字节`、`1,500` 字以内纯文本。
3. **社区零代码共创闭环**：`.github/ISSUE_TEMPLATE/` 提供零 Git 门槛表单，贡献统一落入按需抽样的 `community/`，并受 11 项自动校验门禁守护。
