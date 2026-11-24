# 参与共建《细胞还活着吗》（Cells Alive?）

**「先问细胞，再问问你自己还活着吗。」**
这个开源小项目的生命力，来自每一个正在实验室、工位或电脑前熬过阴性结果、追过新奇现象的同行——不论你是硕博生、博士后、高校教师、科研院所研究员，还是生物医药企业研发从业者。

即使你完全不会用 Git 或终端命令行，也可以在 **1 分钟内**把你的真实瞬间、段子和表情贴纸贡献进来。

---

## 一、两种零门槛投稿方式

### 方式 A：不会 Git 也能投（1 分钟 GitHub Issue 表单）

直接在 GitHub 仓库点击 **Issues → New issue**，按你的内容选对应模板填写即可（维护者会定期整理合入 `community/`）：

- **[科研起落瞬间投稿](.github/ISSUE_TEMPLATE/01-submit-moment.yml)**：分享一次**失落 / 阴性 / “退展”时刻**，或一次**高兴 / 意外发现 / 稳稳过关时刻**——写下当时发生了什么、你最不想听到的假话，以及当时真正能托住你或让你会心一笑的话；
- **[松弛段子 / 原创表情贴纸投稿](.github/ISSUE_TEMPLATE/02-submit-meme-or-sticker.yml)**：分享你们组里或微信群里不油腻的自嘲短句、文字表情卡，或者你自己画的极简纯矢量 SVG 贴纸；
- **[语气火候校准反馈](.github/ISSUE_TEMPLATE/03-tone-calibration.yml)**：觉得哪句太油腻、太冷、太像社科说教、默认了学生身份，或发现任何渗入正式论文的风险，欢迎直接点名纠正。

### 方式 B：直接提交 Pull Request（面向熟悉 Git 的朋友）

1. 编辑对应的社区共创文件（不建议直接往常驻规则加长句子）：
   - 失落 / 阴性 / 退展共创墙：[community/moments-low.md](./community/moments-low.md)
   - 高兴 / 新奇发现 / 过关共创墙：[community/moments-high.md](./community/moments-high.md)
   - 松弛段子与文字表情卡池：[community/memes-and-lines.md](./community/memes-and-lines.md)
   - 原创无版权纯内联 SVG 贴纸：[community/stickers/](./community/stickers/README.md)（单文件须 `<= 8 KB`，零 `<script>` 与外链）
2. 提交 PR 前，请先在仓库根目录运行本地一致性与安全自检：
   ```bash
   python scripts/sync_adapters.py --sync
   python scripts/sync_adapters.py --check
   ```

---

## 二、为什么不会把 AI 上下文越喂越臃肿？（防膨胀架构）

开源人设插件最怕贡献越多、System Prompt 越长，最后把模型注意力全吃光。本项目采用**双层隔离**：

- **常驻微规则（`core/micro-rule.md`）永远锁定在 `<= 35 行 / <= 2,000 字节`**：社区投稿**不会**塞进常驻提示词；
- **`community/` 仅作为按需抽样灵感池**：Agent 仅在需要语感校准或补充松弛点缀时轻量参考几条，**严禁整库读入常驻上下文，也严禁逐字复读固定台词**。

---

## 三、四条社区审核底线

1. **版权干净**：仅接受**本人原创**、或明确以 **MIT / CC0** 授权的段子与纯矢量 SVG 贴纸；**严禁直接搬运或上传有版权争议的商用微信表情包截图**。
2. **底线清醒**：严禁任何把“删离群点凑显著”“P 值美化”“编造数据”当笑话或合理化的投稿。
3. **保护隐私、禁止挂人**：投稿请隐去真实课题组、导师姓名、单位或未发表具体数据，不得借投稿进行人身攻击。
4. **真实平实、留一点呼吸感**：我们记录真实的实验与生信卡点，也留住探索的新奇微光；拒绝戾气宣泄或空洞鸡汤。

---

## 贡献者与致谢

- **Zhuocheng Yao**（[@Spark-xY6](https://github.com/Spark-xY6)）：插件发起人、核心规则与适配器工程实现。
- **Xuehua Zhao**（GitHub: [@snowflakee685-commits](https://github.com/snowflakee685-commits)）：提供了社会工作方面的专业建议，用于优化技能中 AI 与人的联结和陪伴感。

---

## Quick English Contributing Note

New moments, relaxed lab expressions, tone calibrations, and original MIT/CC0 inline SVGs are warmly welcome via `.github/ISSUE_TEMPLATE/` (zero-Git) or PRs into `community/`. Before opening a PR, please ensure `python scripts/sync_adapters.py --check` passes with exit code `0`.
