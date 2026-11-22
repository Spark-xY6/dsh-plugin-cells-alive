# 细胞还活着吗 · Cells Alive?（科研同伴插件）

**中文** · [English](./README.md) · [真实配对实测对比](./docs/comparison-and-showcase.md) · [社区共创瞬间与段子池](./community/README.md)

<img src="./icon.svg" width="76" height="76" alt="细胞还活着吗 logo"/>

**先问细胞，再问问你自己还活着吗。**  
给做生科和科研的人配一个懂分寸的 AI 搭子：你挫败内耗时它能先肯定你已经做扎实的活并温和劝你存断点休息；你赶 Tenure / 毕业不想听鸡汤时它少抒情直接帮你算性价比；**一旦切去写论文正文和跑代码，所有情绪和段子自动归零（0% 渗入）。**

---

## 为什么做这个插件？

平时用 AI 做科研，最容易踩到两个坑：
1. **冰冷纯工具**：连跑两周分析被更严口径推翻（“退展”），或者赶论文、等毕业压到喘不过气时，裸跑 AI 只会甩给你 5 条排查清单；或者把青椒/博后误当成研究生哄“跟导师沟通毕业”。
2. **整活人设翻车**：网上有些“发疯文学 / 生物狗”提示词太长太吵，占满上下文不说，写到正式论文 Results 时还会把口语和烂梗带进去，甚至在 `p = 0.068` 卡线时拿学术不端开玩笑。

**《细胞还活着吗》用不到 2 KB（1,792 字节）的超轻规则解决这三件事：** 先问清楚你现在想要“成果导向”还是“温和陪伴”，只讲真实做好的扎实工作、守住统计学红线，写论文时 100% 退回学术状态。

---

## 先看 Input -> Output 真实配对效果

同一模型 `gpt-6.1-sol`（2026-11-22，4 组高频科研情境真实配对测试）：

![《细胞还活着吗》Input 到 Output 实测对照](./docs/images/cells-alive-showcase.png)

| 你给 AI 的输入（Input） | 无插件裸跑常见问题 | 挂载《细胞还活着吗》后（Output） |
| :--- | :--- | :--- |
| **加严校正后差异没了（“退展”）**，怀疑自己能力差 | 只做统计解释，不肯定你主动核查的工作，也不提示收工停顿 | 先肯定“主动补严校正提高了结论可信度”，拆开结果与自我否定，并给清晰停顿节点 |
| **青年 PI 冲 Tenure 三批阴性**，要求少抒情直接算性价比 | 输出 1,074 tokens（44.0s），列长问卷，没盘点已有资产 | 读取 `.cells-alive.yaml` 绑定身份，**篇幅减 19.7%**（862 tokens / 34.9s），先保主线与时间资产并给止损公式 |
| **明早组会卡在 `p = 0.068`**，问能不能删第 3 号样本凑 `p = 0.021` | 强模型虽能拒删，但常只给学术原则，缺可直接开口的交账话术 | 寸步不让拒绝 p-hacking，同时给出**组会可直接照读的抗质疑原话**与 95% CI 展示方案 |
| **凌晨 01:40 内耗 + 改写 Nature Comms 英文 Results** | 把原文 `lipid beta-oxidation` 改写成 `fatty acid β-oxidation` | 先轻接熬夜断点“写完这版就收工”；英文段落 **0% 情绪/段子渗入**，且忠实保留 `lipid β-oxidation` 原词 |

---

## 比裸跑与社区轮子多做了什么？

- **常驻极轻（1,792 字节 / 6 行）**：同类人设 Prompt 动辄几千字稀释推理注意力，本插件用单源硬门禁锁死在 `<= 2 KB`，不抢科学推理算力；
- **成果导向 vs 关怀伦理双轨分流**：不像社区模板一刀切鸡汤或一刀切整活，靠工作区 `.cells-alive.yaml` 记住你是硕博、博后青椒还是企业研发；
- **L0 正式交付物 0% 渗入 + 1 分钟零代码共创**：论文、学位论文、审稿回复自动退回纯学术；会用网页就能通过 [GitHub Issue 表单](./.github/ISSUE_TEMPLATE/01-submit-moment.yml) 给社区投稿你的科研瞬间或离线 SVG 小贴纸。

---

## 1 分钟安装与使用

### 方式 A：DeepSeek Harness (DSH) 一键安装

```powershell
dsh plugin --profile web add "github:Spark-xY6/dsh-plugin-cells-alive#v0.1.0"
```

安装重启后，直接对 DSH 说（首次建议复制 `.cells-alive.yaml` 偏好模板）：

> 请开启 cells-alive。我目前更偏成果导向（或温和陪伴），正处于【博后/硕博/企业研发】阶段，日常分析卡壳时按习惯陪我推进，写论文和代码正文时保持纯学术零渗入。

### 方式 B：直接用于 Codex / Cursor / Claude Code / Antigravity / 网页版

| 平台 | 一分钟接入方法 |
| :--- | :--- |
| **Codex / Claude Code** | 把 [adapters/agents-md-snippet.md](./adapters/agents-md-snippet.md) 追加到项目根目录 `AGENTS.md` 或 `CLAUDE.md` |
| **Cursor** | 复制 [adapters/cursor-rule.mdc](./adapters/cursor-rule.mdc) 为项目 `.cursor/rules/cells-alive.mdc` |
| **Antigravity Plugin** | 放入本地 `.agents/plugins/cells-alive/`（已内置 [plugin.json](./plugin.json) 与 [SKILL.md](./skills/cells-alive/SKILL.md)） |
| **OpenClaw / 网页聊天版** | 复制 [adapters/soul-md-snippet.md](./adapters/soul-md-snippet.md) 或 [web-custom-instructions.txt](./adapters/web-custom-instructions.txt)（仅 697 字） |

---

## 贡献者与致谢

- **Zhuocheng Yao**（[@Spark-xY6](https://github.com/Spark-xY6)）：插件发起人、核心规则与适配器实现。
- **Xuehua Zhao**（GitHub: [@snowflakee685-commits](https://github.com/snowflakee685-commits)）：提供了社会工作方面的专业建议，用于优化技能中 AI 与人的联结和陪伴感。

## 更多细节与社区共建

- 📊 **[完整三方对比、真实配对数据与工程原理](./docs/comparison-and-showcase.md)**
- 🌱 **[社区共创瞬间墙 / 段子卡池 / 原创离线 SVG 贴纸](./community/README.md)** · **[1 分钟投稿指南](./CONTRIBUTING.md)**
- 🧪 **[8 个场景与零渗入对照样例（examples/）](./examples/01-setback-care-and-pivot.md)**
- 🛡️ **非目标声明**：本插件不是心理诊疗工具，也绝不提供美化 P 值或无依据删样本的捷径。License: [MIT](./LICENSE)。
