# 细胞还活着吗 · Cells Alive? (`dsh-plugin-cells-alive`)

[English](README.en.md) · [免安装离线体验页](adapters/start.html) · [对比测评与实测](docs/comparison-and-showcase.md) · [共创征集](community/README.md)

<img src="./icon.svg" width="64" height="64" alt="Cells Alive? 图标"/>

*先问细胞，再问问你自己还活着吗。「科学是服务于人的」——首先照顾好自己，不弄得苦大仇深。*

**做湿实验养细胞、跑生信等集群卡壳到深夜时，它像一位懂科研、不爱说教的同伴：受挫时用平实温热的话先把你接住、看见已经做扎实的工作，推进时只给 1 个低负担小抓手；绝不乱猜身份、绝不放水统计底线，切回写正式论文与代码时强制 0% 口语或段子渗入。**

![真实科研受挫对话实测：理解而不评判、不催清单，切回论文零渗入](docs/images/cells-alive-showcase.png)

## 怎么开始（三种方式任选，无需配置也能用）

| 你现在在哪用 AI | 30 秒上手方式 |
| --- | --- |
| **网页版 ChatGPT / Claude / DeepSeek** | 双击打开完全离线的 [adapters/start.html](adapters/start.html)，写一句自己的话（或选实验室场景片，也可留空）点「复制到聊天」，贴进对话即可。内置「**深夜台灯**」护眼模式、纯本机保存的「**干净断点便签**」与偏好生成器。 |
| **DeepSeek Harness (DSH)** | 运行 `dsh plugin --profile web add (Resolve-Path '.\dsh-plugin-cells-alive-0.3.0.tgz').Path` 后重启即可，零依赖。 |
| **Codex / Claude Code / Cursor** | 直接复用随包同步的 [AGENTS 片段](adapters/agents-md-snippet.md)、[Cursor 规则](adapters/cursor-rule.mdc) 或 [.claude-plugin/plugin.json](.claude-plugin/plugin.json)。 |

## 为什么做、有什么用与实测效果

- **告别“抱抱你 + 甩三步清单”的焦虑制造机**：真实同学 A/B 盲测显示，实验做了论文却在短促沟通里被否定时，常规 AI 套话开场后紧接着丢出三步整改清单（甚至冒出评判标签）只会让人更焦灼。本插件融合社会工作 **理解而不评判**（非评判性共情）建议，核心规则精炼至 **6 行 / 不到 2 KB**（网页版 `741` 字），不占模型主推理注意力。
- **不猜身份、按场景切换语气**：不默认问问题的人就是研究生，通过可选 `.cells-alive.yaml` 兼容硕博、博后、青椒、研究员与企业研发；情绪倾诉先接住再轻回课题，青年 PI 成果导向模式下冗余分析篇幅下降约 **19.7%**（响应提速约 **20.7%**），平静问数据时零多余寒暄。
- **守住学术红线，正稿 0% 渗入**：面对卡在 `p = 0.068` 想删异常样本，温和而坚定地守住对照与统计学门槛，同时附上组会可直接复述的全样本 + 95% CI 敏感性分析方案；切换写英文论文 Results、审稿回复、基金、对外 PPT 与代码正文时 **0% 情绪或梗渗入**，实测原样保住 `lipid β-oxidation` 等术语不被篡改。

## 致谢与边界

- **Zhuocheng Yao** ([@Spark-xY6](https://github.com/Spark-xY6)) —— 作者、核心规则设计与跨端适配。
- **Xuehua Zhao** ([@snowflakee685-commits](https://github.com/snowflakee685-commits)) —— 社会工作视角的人机连接、陪伴克制与真实支持指导。
- 欢迎通过 [GitHub Issue 模板](community/README.md) 投喂你的科研瞬间。本插件并非临床心理医疗服务，也绝不赞同无依据删点或 p-hacking。[MIT License](LICENSE)
