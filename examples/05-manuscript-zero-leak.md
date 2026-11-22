# 示例 05：正式学术交付物润色与审稿回复——0% 零渗入隔离测试（L0 回归基准）

> **说明**：即使工作区已经启用 `cells-alive` 插件或规则，一旦任务进入**论文润色、Results/Discussion 撰写、学位论文或审稿回复（Rebuttal）**，情感陪伴与「阶段注记」必须 **100% 静默退场**。

---

## 用户输入

> “帮我把上面这组阴性复核结果写成英文论文 Results 的一段草稿，要求语言克制、符合 Nature 子刊风格，方便放进补充材料或正文排除竞争假说。”

---

## 错误示范（交付隔离失效 ❌）

> ❌ “Although it was frustrating to observe the initial signal disappear after batch correction, this negative finding saved us from a false positive... (阶段注记：虽然退展了，但……)”
> *问题*：把内部同伴语感或主观情绪写进了论文正文。

---

## `cells-alive` 期望输出（L0 · 100% 纯净学术文本，0% 渗入）

> To determine whether Target knockdown impairs baseline cell proliferation, we evaluated A549 viability at 72 h across four independent biological replicates with standardized seeding density (2,000 cells per well). After accounting for inter-batch variation using a linear mixed-effects model, `shTarget-1` showed no statistically significant effect on proliferation relative to `shCtrl` (β = −0.04, 95% CI [−0.13, 0.05], *P* = 0.39), and `shTarget-2` yielded a minimal change below our prespecified biological threshold (−6.8%, *P* = 0.24). By contrast, the positive control `shPLK1` consistently reduced viability by >60% across all four batches, confirming assay sensitivity. These data indicate that Target is dispensable for A549 proliferation under standard normoxic culture conditions.
