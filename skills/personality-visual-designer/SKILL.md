---
name: personality-visual-designer
description: >-
  人格认知测评报告的现代极简人文美学视觉设计子 Skill（Editorial & Minimalist Aesthetic Engine）。
  负责将心理学心智数据转化为具备现代出版物级美感、低饱和矿物调色盘、LLM 现场编写的淡雅几何线条背景意象（SVG）与精粹心智格言的流式 HTML 档案。
---

# 人格报告美学视觉设计子 Skill (Personality Visual Designer)

本 Skill 是人格测评系统的**美学视觉总监（Art Director）**。
它专门解决传统数据报告“界面花哨、配色俗艳、缺乏设计感”的痛点，确立了一套**现代极简人文出版与理性网格版式**的高级视觉规范。

---

## 核心设计哲学 (Aesthetic Philosophy)

1. **纸张般的温润低饱和质感 (Warm Low-Saturation Paper Canvas)**：
   - 告别高饱和发光渐变与深色电竞毛玻璃；
   - 采用温润如古董纸张的暖白/浅亚麻底色（如 `#FAF9F5` / `#F7F5EE`），搭配高清晰度的炭黑油墨排印文字（`#191919`），带来宁静典雅的书卷气息与极高的阅读舒适度。
2. **极简线条与理性网格版式 (Architectural Grid & Monospace Accents)**：
   - 采用克制的细线条边界（`1px border #E5E2DA`）与清晰的网格对齐；
   - 融入等宽字体（Monospace）的注释标签（如 `01 / COGNITIVE ENGINE`、`#instinct-sp`），营造前沿学术研究的理性严谨感。
3. **LLM 现场编织专属几何矢量背景 (LLM Prompt-to-SVG Ambient Metaphor)**：
   - 彻底摒弃静态死板模板；
   - 由负责生成报告的 LLM 结合用户在整个长程对话中流露出的独特精神意象（如：沙盘因果网、真理哨所、天体星轨、棱镜折射、自相似黄金螺旋等），**现场自主手绘一段 20~30 行极简、轻盈的纯线条 SVG 代码**，作为淡雅水印（Watermark）嵌入卡片右下角背景，实现真正的千人千面。
4. **一句话底层心智哲学格言 (Philosophical Anchor Quote)**：
   - 为每种人格心智架构提炼一句兼具文学意蕴与认知穿透力的格言，醒目烙印在报告扉页。
5. **自上而下纯净流式阅读 (Sequential Vertical Flow)**：
   - 摒弃打断阅读节奏的 Tab 标签切换，采用自然向下滑动的单页流式布局，结构层层递进，一气呵成。

---

## LLM 现场编写 SVG 代码规范指南 (SVG Generation Heuristics)

当 LLM 进入视觉生成步骤时，必须严格遵守以下 SVG 编写法则：

### 1. 基础容器与属性
```html
<svg viewBox="0 0 400 240" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <!-- 内部几何线条元素 -->
</svg>
```

### 2. 线条与色彩约束
- **调色引用**：直接使用 CSS 变量，确保线条与动态色盘完美契合：
  - 主要轮廓线：`stroke="var(--primary)"`，线条粗细建议 `stroke-width="1.2"` 或 `stroke-width="1.5"`，不透明度 `stroke-opacity="0.7"` ~ `0.9`；
  - 辅助网格/参考轴线：`stroke="var(--secondary)"` 或 `stroke="var(--primary)"`，建议附带虚线 `stroke-dasharray="3 3"` 或 `stroke-dasharray="2 2"`，透明度较低（`stroke-opacity="0.2"` ~ `0.4`）；
  - 极少量的微几何填充：`fill="var(--secondary)" fill-opacity="0.08"` 或小圆点锚点 `fill="var(--primary)"`。
- **纯粹线条美学**：只使用 `<line>`, `<circle>`, `<rect>`, `<path>`, `<polygon>` 等基础几何构件，严禁出现厚重的大面积色块或渐变。

### 3. 自由意象构想与几何转化原则 (Unconstrained Metaphor & Geometric Synthesis)
- **释放 LLM 艺术创造力，严禁机械死板套用模板**：
  - 严禁死板规定某种功能或型号“只能画某种图案”！每位受测者在长程对话中流露出的生活经历、职业背景、深层焦虑与精神向往都是独特的。
  - LLM 应自由提取该受测者最本真、最具穿透力的核心心智意象（例如：天文浑天仪、双星引力轨道、多面体晶体解构、拓扑流形切片、声学琴弦驻波、古典拱券透视、群岛洋流等等，皆可自由挥洒）。
- **几何抽象化法则（How to Abstract）**：
  - 将脑海中的概念具象“极简骨架化”：通过基础几何线条（细直线、优雅圆弧、正多边形、同心圆、微弱刻度虚线）进行数学抽象；
  - 重点在于营造一种**“克制、精密、静谧”的理性艺术美感**，与纸张底色和谐相融，充当右下角若隐若现的精神图腾。

---

## 视觉资产与模块架构

```text
personality-visual-designer/
├── SKILL.md                          # 视觉子 Skill 核心规约与 LLM SVG 生成指南
├── README.md                         # 视觉系统设计手册
├── references/
│   └── editorial_aesthetic_guide.md  # 详细调色盘字典、SVG 几何意象图谱库与排版基准
├── resources/
│   └── editorial_report_template.html# 现代极简流式阅读 HTML 模版
└── scripts/
    └── theme_generator.py            # 辅助调色计算与 SVG 合成工具
```
