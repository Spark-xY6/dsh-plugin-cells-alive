# 原创离线 SVG 贴纸库（Community SVG Stickers）

本目录用于收集生科同行原创的极简、温暖或带一点自嘲松弛感的纯矢量 SVG 贴纸（可在内部自用 `.html` 分析报告收尾处按需嵌入，100% 离线可用）。

## 已有原创贴纸

| 文件名 | 主题 | 适用情境 | 许可 |
| :--- | :--- | :--- | :--- |
| [chill-cell-pause.svg](./chill-cell-pause.svg) | 「先到这，出去走走」淡定小细胞 | 卡点收工、引导放空或深夜存好断点后 | MIT |
| [curious-cell-spark.svg](./curious-cell-spark.svg) | 「居然真是这样」亮灯小细胞 | 首次看到意外现象或机制线索的新奇时刻 | MIT |

## 投稿硬规范（PR / Issue 必过自动检查）

1. **版权零争议**：必须为投稿者**本人原创**或 **CC0 / MIT** 明确授权作品；严禁将微信商用表情包截图或他人版权插画描图/内嵌进仓库；
2. **100% 离线安全 SVG**：
   - 严禁包含 `<script`、事件回调属性（如 `onload=`/`onclick=`）或 `<foreignObject>`；
   - 严禁包含 `http://`、`https://` 或 `file://` 等外部链接与字体拉取；
   - 严禁在 SVG 内嵌入巨大 Base64 位图；单文件体积须 **`<= 8 KB`**；
3. **明暗主题可读**：优先透明底、简洁粗细均衡的线条与中文字体回退栈（`-apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", sans-serif`）。
