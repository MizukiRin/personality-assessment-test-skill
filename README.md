# 人格认知测评与心智建模专家 Skill (Personality Assessment Test)

这是一个基于严肃**分析心理学（荣格八维动力学 / 毕比原型心智模型）**与**现代动态九型人格系统（三中心、27种副型序列、三元组防御阶梯）**的深度人格测评与心智建模 Agent Skill。

---

## 核心设计特性

1. **长程沉浸式自然对话（12~18+ 轮交互）**：
   - 彻底摒弃机械式、选择题式静态题库；
   - 采用多轮螺旋收敛机制，从冷启动了解受测者生活语境开始，层层递进深入心智底层。
2. **动态情境嫁接（Dynamic Scenario Weaving）**：
   - 将心理学学术测量目标（不变量）与用户的真实生活坐标（可变量：如不同职业、学生、家庭结构等）动态结合；
   - 实时生成贴合用户现实、具备真实摩擦力的高张力两难生活切片，诱导潜意识第一直觉体感浮出水面。
3. **三段式透明反馈协议（Three-Part Turn Protocol）**：
   - 每一轮提问皆包含：`【线索镜映与捕获】` ➔ `【理论归因与排他依据】` ➔ `【定向定制情境探针】`；
   - 测评逻辑与学术依据全程对用户公开透明，拒绝巴纳姆效应。
4. **八维 × 九型复合动力学与跨型号对比**：
   - 深入分析当前荣格八维 + 九型人格组合的典型行为特质与思维定式；
   - 重点对比“同一套 MBTI 八维在搭载不同九型主型号时”的显著差异与外显风貌；
   - 提供该复合心智架构的天然擅长领域、最佳工作协作模式与心智跃升指引。
5. **双模报告交付与动态心智色彩学 UI**：
   - 同时支持生成纯文本 Markdown 档案与自包含的精美 HTML 交互大屏；
   - **动态心智调色盘**：由 LLM 深度分析受测者的 MBTI 认知属性与九型能量底色，动态构思并注入专属主题色盘（主色、辅色、强调色、渐变背景及色彩心理学解读）；
   - 支持 Tab 标签页切换、多色功能栈卡片，以及一键打印/导出高清 PDF。

---

## 目录文件结构

```text
personality-accessement-test/
├── SKILL.md                          # [核心大脑] 规范长程对话状态机、三段式协议、动态出题与调色规则
├── README.md                         # [项目概览] Skill 架构说明与使用文档
│
├── references/                       # [学术基石与诊断指南] 供 Agent 渐进式按需查阅
│   ├── mbti_cognitive_functions.md   # 荣格 1921、迈尔斯 1980、毕比 2004 模型与昆克劣势暴走理论
│   ├── enneagram_dynamics.md         # 里索-赫德森九型、纳兰霍防御机制、27副型与三元组防御阶梯
│   └── probing_methodology.md        # 动态情境编织法则、八维/九型线索捕获指标与复合动力学分析规范
│
├── resources/                        # [双模资源模版]
│   ├── report_template.md            # Markdown 纯文本全景档案模版
│   └── report_template.html          # 动态配色交互式 HTML 报告大屏模版
│
├── scripts/                          # [辅助工具脚本]
│   ├── scoring_engine.py             # 16种类型八维功能位阶映射与副型计算引擎
│   └── generate_report.py            # 支持 MD + HTML 双模自动渲染生成工具
│
└── skills/                           # [内置子 Skill 目录] 独立封装的专业能力模块
    └── personality-visual-designer/  # 负责低饱和调色盘、SVG 背景意象与美学排版的子 Skill
        ├── SKILL.md                  # 视觉子 Skill 规范与 LLM SVG 生成指南
        ├── README.md                 # 视觉系统设计手册
        ├── references/
        │   └── editorial_aesthetic_guide.md # 详细调色盘字典与 SVG 图谱库
        ├── resources/
        │   └── editorial_report_template.html # 极简流式阅读 HTML 模版
        └── scripts/
            └── theme_generator.py    # 调色计算与 SVG 合成辅助脚本
```

---

## 使用与集成方式

作为 Antigravity / Claude Agent Skill 使用：
当用户提出性格测评、深度八维探索或心智分析需求时，Agent 会自动载入 [`SKILL.md`](./SKILL.md)，以专业咨询师身份开启多轮自然对话探索。
