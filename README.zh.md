# 细胞还活着吗 · Cells Alive?

[English](README.md) · [完整对比数据](docs/comparison-and-showcase.md) · [社区瞬间墙](community/README.md) · [1 分钟投稿](CONTRIBUTING.md)

<img src="./icon.svg" width="72" height="72" alt="细胞还活着吗"/>

*先问细胞还活着吗，再问问自己还活着吗。*

做实验或者通宵跑分析做久了，每天都在盯着培养箱、条带和卡住的脚本转，很容易忘了停下来吃口饭、睡一觉。而真对着常见 AI 吐句苦水时，它往往丢回上千字的“一二三步反思清单”，甚至在不知道身份时默认管你叫“学生”；如果换成网上很吵的搞笑人设模板，又会挤占模型记忆，写到论文正文字里行间还会漏出几句轻飘飘的网络梗。

这个只有 **6 行、1,948 字节**常驻规则的小插件想做的事很简单：聊天时听得懂实验室里的真实难处与日常黑话，以理解而不评判的分寸先把人接住——情绪上头时不抢跑甩“三步行动清单”催焦虑，不贴标签也不充当心理咨询师；切回写论文正文或代码时，立刻退回干净严谨的学术状态。

## 实际用起来是什么感觉

下面这组真实受挫对话来自最新 1,948 字节规则的盲测对照（不贴评判标签、不抢跑甩三步清单，也不把对话拉成心理课）：

![研究写了论文却被导师匆匆否定后，最新版《细胞还活着吗》的真实防焦灼回应](docs/images/cells-alive-showcase.png)

同样的陪伴分寸，在另外三个高频节点也很直观：

- **明早组会差一点，想把最差的 3 号样本先删掉**：常见 AI 往往只顾着警告“属于 cherry-picking，会被查处”，却不管明天的汇报怎么办。插件会先肯定你已经实打实跑完了 4 批独立重复、看清整体规律，然后坚决守住不删无硬伤样本的底线，同时直接帮你把明天 PPT 能用的结构写出来——用“全样本主图 + 旁注敏感性对比”透明交代波动，最后顺手提醒周末赶完早点睡。
- **凌晨 1:40 改图累到想放弃，顺手让润色一段英文 Results**：先轻声拆开“今晚图没调顺”和“核心结果早已成立”，叫停先存版本去睡；紧接着交付的英文正文只有纯粹的学术表达，连原文里的 `experimental animals` 都不擅自改动，聊天口语零渗入：

> Compared with the control group, probiotic supplementation for 4 consecutive weeks significantly shortened sleep onset latency and increased the proportion of nocturnal slow-wave sleep in experimental animals.

- **带队老师（PI）考核只剩 8 个月，希望别安慰直接算投入产出比**：工作区读取到 `.cells-alive.yaml` 里的 `outcome_driven` 与 `pi` 阶段后，完全不把老师当学生哄——开篇直接把“主线稿件已投出”与“三条探索线跑满三批刚好止血”盘清成确定筹码，拍板把 70% 以上精力锁回主线，最多只留一条设 1 轮两三周的最小验证死线；不像裸跑 AI 在算完后结尾又反抛回 5 个待补充问题。

## 为什么能一直保持清醒和好感

插件并没有把大量语录塞进每次对话的系统提示里，而是把底层规则严格锁在 `core/micro-rule.md` 的 **6 个非空行（1,948 字节）**之内，不抢科学推理的上下文注意力，并由脚本自动同步到 **DSH、Codex、Claude Code、Cursor、Antigravity 与网页端自定义指令** 6 套适配器，保持零漂移。

社区里收集的那些会心一笑的日常表达——比如“先问细胞还活着吗，再问问自己还活着吗”“问题不会连夜长腿跑掉，先去走两步”“允许今天先停在半路上”——只作为按语境化用的灵感池存在，不会每次对话机械背台词，也不会带进任何正式文档或学术不端玩笑里。如果你也想加一两句属于自己实验室的瞬间或极简 SVG 小贴纸，不会 Git 也能直接点网页 [GitHub Issue 表单](.github/ISSUE_TEMPLATE/01-submit-moment.yml) 投稿。

## 1 分钟安装与启用

在 DeepSeek Harness (DSH) 中安装并重启对应 profile：

```powershell
dsh plugin --profile web add "github:Spark-xY6/dsh-plugin-cells-alive#v0.1.0"
```

启用后可以把 [templates/cells-alive.yaml.example](templates/cells-alive.yaml.example) 复制到项目根目录改名为 `.cells-alive.yaml`（可选），直接告诉助手你现阶段的习惯即可：

> 请开启 cells-alive。我目前更偏成果导向（或温和陪伴），正处于【博后/硕博/企业研发】阶段，日常分析卡壳时按习惯陪我推进，写论文和代码正文时保持纯学术零渗入。

如果你平时不用 DSH，也可以直接取用同一规则同步出的单文件适配：

- Codex / Claude Code：把 [adapters/agents-md-snippet.md](adapters/agents-md-snippet.md) 追加到项目根目录 `AGENTS.md` 或 `CLAUDE.md`（或使用 [.claude-plugin/plugin.json](.claude-plugin/plugin.json)）
- Cursor：复制 [adapters/cursor-rule.mdc](adapters/cursor-rule.mdc) 为 `.cursor/rules/cells-alive.mdc`
- Antigravity：放入本地插件目录，直接加载内置 [plugin.json](plugin.json) 与 [SKILL.md](skills/cells-alive/SKILL.md)
- OpenClaw / 网页版聊天框：复制 [adapters/soul-md-snippet.md](adapters/soul-md-snippet.md) 或仅有 741 字的 [web-custom-instructions.txt](adapters/web-custom-instructions.txt)

## 贡献者、致谢与边界

- **Zhuocheng Yao**（[@Spark-xY6](https://github.com/Spark-xY6)）：插件发起人、核心规则与跨平台适配器实现。
- **Xuehua Zhao**（GitHub: [@snowflakee685-commits](https://github.com/snowflakee685-commits)）：提供了社会工作方面的专业建议，帮助插件把人机之间的联结感、共情分寸与陪伴温度做得更加自然克制。

更多原始配对实验（含 `gpt-6.1-sol` 4 组完整对照与 8 个场景样例）见 [docs/comparison-and-showcase.md](docs/comparison-and-showcase.md) 与 [examples/01-setback-care-and-pivot.md](examples/01-setback-care-and-pivot.md)。本插件不是心理诊疗工具，也绝不提供美化 P 值或无依据删样本的捷径，代码以 [MIT 协议](LICENSE)开源。
