# 人格报告美学视觉设计子 Skill (Personality Visual Designer)

这是一个专为心理学认知档案定制的**现代极简人文排印美学子 Skill**。
设计语言深度结合现代出版物编排与极简线条排版，彻底告别俗艳的高饱和渐变，回归有温度、有呼吸感的人文出版级质感。

---

## 核心设计特性

1. **温润低饱和矿物纸张画布 (Warm Mineral Paper Canvas)**：
   - 以古董羊皮纸暖白（`#FAF9F5`）为基底，搭配纯净白纸卡片（`#FFFFFF`）与浅亚麻灰衬底（`#F4F1EA`）；
   - 正文采用深度油墨炭黑（`#191919`），文字间距舒展自然，极具阅读舒适度。
2. **古典与数理几何线条背景意象 (Subtle Ambient SVG Metaphors)**：
   - 告别抽象模糊插画，将精密矢量线稿（多立克石柱轴线、航海星盘经纬、黄金螺旋曲面、网格拼贴）作为**低透明度淡雅水印**融入卡片背景中，呈现若隐若现的结构之美。
3. **一句话底层心智哲学格言 (Philosophical Anchor Line)**：
   - 为每份报告提炼一句富有智性穿透力的专属题词，展现人格深层精神意境。
4. **纯净向下滑动的顺序阅读排版 (Sequential Scroll Flow)**：
   - 摒弃打碎阅读体验的 Tab 标签页切换，采用清晰的五大板块纵向流式排版，结构层层递进。
5. **极简等宽字符注释 (Monospace Accents)**：
   - 细线边框（`1px #E5E2DA`）搭配等宽字体标签（`01 / COGNITIVE ENGINE`、`#instinct-sp`），兼具科技理性与学术典雅。

---

## 目录结构

```text
personality-visual-designer/
├── SKILL.md                          # 视觉子 Skill 规范与调度手册
├── README.md                         # 本说明文件
├── references/
│   └── editorial_aesthetic_guide.md  # 详细调色盘字典、SVG 几何意象图谱库与排版基准
├── resources/
│   └── editorial_report_template.html# 现代极简流式阅读 HTML 模版
└── scripts/
    └── theme_generator.py            # 低饱和调色盘计算、专属背景 SVG 意象与格言生成引擎
```

---

## 快速使用

在主 Skill 生成报告时自动调用，亦可单独运行生成测试预览：

```bash
python scripts/theme_generator.py
```
