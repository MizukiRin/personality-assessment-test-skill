# Personality Assessment Test (人格认知测评与心智建模专家)

> 基于严肃分析心理学（荣格八维 / 毕比原型模型）与现代动态九型人格（三中心、27 副型、三元组），通过沉浸式多轮自然对话推演底层心智架构，并交付现代极简美学双模报告的 AI Agent Skill。

## ✨ 核心功能 (Features)

* **双轨制自然咨询架构**：前台保持 100% 温和敏锐的心理咨询式聊天（零学术说教与生硬标题），后台同步动态维护 `outputs/clue_tracking_dossier.md`，完整沉淀每一轮的心理学探针意图、线索捕获与文献排他证据链。
* **动态情境嫁接与梯级延伸**：彻底摒弃静态选择题库，基于用户当下的生活坐标与实时对话细节，动态编织高摩擦力生活两难切片，支持从粗粒度身份自然延伸到滚雪球式贴身定制。
* **九型防火墙与控制变量验证**：锁定核心动机（Why）并自动拉起九型特性黑名单，阻断动机噪音向八维认知工具（How）的污染；通过现实客观碰撞三公理（第一干预动作、终局意图、职业耻感锚点）逼出认知手段分叉。
* **反人格面具与语义消歧协议**：内置前后逻辑冲突检测与社会合规/创伤噪音剥离，通过温和镜映穿透自我美化；禁绝空洞哲学隐喻，强制绑定身体体感与情绪底色，消除人机语义错位。
* **跨系统复合消歧与劣势动作验真**：预装 8 大高混淆复合原型消歧矩阵（如 5号+J、1号+P、3号+P、6号+N、8号+Ti/Fi 等）以及 Naomi Quenk 8 大劣势功能实操行为还原库，形成严谨的终审闭环。
* **极简人文美学双模报告与自动归档**：内置 `personality-visual-designer` 视觉子 Skill，一键交付 Markdown 纯文本深度档案与现代低饱和纸质排印流式 HTML 报告（含 LLM 现场手绘几何线条 SVG 水印与专属格言），并自动按时间戳归档历史测评记录。

## 🛠️ 前置条件 (Prerequisites)

在使用本 Skill 前，请确保本地已满足以下环境要求：

* **支持的 AI 工具**：Antigravity / Claude Code / Cursor / Windsurf / 其他支持 `SKILL.md` 规范的 Agent
* **依赖工具**（用于运行本地双模报告渲染脚本）：
  * `Python` >= 3.8（仅依赖标准库，无需额外安装第三方包）

## 📦 安装方法 (Installation)

### 方式一：通过 CLI 一键安装（推荐）

```bash
npx skills add MizukiRin/personality-assessment-test-skill
```

### 方式二：手动安装

将本仓库下载或克隆到你的全局/项目 Skills 目录中：

```bash
# 全局安装（所有项目可用，以 Claude Code 为例）
git clone https://github.com/MizukiRin/personality-assessment-test-skill.git ~/.claude/skills/personality-assessment-test

# 或仅在当前项目安装
git clone https://github.com/MizukiRin/personality-assessment-test-skill.git .claude/skills/personality-assessment-test
```

> 若在 Antigravity 中作为 Plugin 使用，可将仓库同步至全局插件目录（如 `~/.gemini/config/plugins/personality-assessment`）。

## 🚀 使用方式 (Usage)

安装完成后，你可以通过**自然语言描述**或**斜杠命令**触发此 Skill：

### 常见触发示例

* **基础全面探索**：
  > “帮我做一次深度人格认知测评，探索我的荣格八维与九型人格架构。”
* **结合现实困扰探索**：
  > “最近在工作协作和未来方向上很内耗，帮我用性格测评深度剖析一下底层心智模式和适合的发展方向。”
* **生成可视化档案 / 复盘线索**：
  > “测评结束了，请帮我生成极简排版风格的 HTML 报告和 Markdown 全景档案。”
* **斜杠命令触发**（如已配置显式命令）：
  > `/personality-assessment-test`

### 输出示例

测评完成后，系统将自动交付 **Markdown 全景档案**、**现代极简流式 HTML 交互大屏**与**后台线索追溯日志**：

```text
# 全景人格认知与心智操作系统档案
> 用户昵称：Rin
> 评定日期：2026-11-20
> 核心类型结论：INTJ (建筑师 / 战略家) · 九型 5w6（5-8-3）副型 sp/sx (so-blind)

【终审认知心智架构】
主导功能 (Hero)：Ni (内倾直觉) — 终局宏观洞察、底层因果、顶层沙盘收敛
辅助功能 (Parent)：Te (外倾思考) — 系统规则架构、SOP 防灾排雷、实效闭环落地
第三功能 (Child)：Fi (内倾情感) — 永恒之童、深层纯粹价值观与安全护城河
第四劣势 (Inferior)：Se (外倾感觉) — 物理杂事高启动阻抗、高压感官代偿暴走
第七盲区 (Trickster)：Fe (外倾情感) — 社交寒暄快速耗电、人情世故天然脱敏

[OK] 成功生成: outputs/personality_profile.md
[OK] 成功生成: outputs/personality_profile.html
[Archive] 本次测评全景档案已安全归档至: outputs/archive/20261120_155900_Rin
```

## 📂 目录结构 (Directory Structure)

```text
personality-accessement-test/
├── SKILL.md                          # 核心指令集（双轨对话协议、高阶出题公理与五阶段状态机）
├── README.md                         # 使用说明文档（本文件）
├── plugin.json                       # 插件清单元数据（用于 Antigravity 等插件生态集成）
├── assets/                           # 插件图标等静态资源
├── references/                       # 严肃心理学理论基石与探针方法论（渐进式按需查阅）
│   ├── mbti_cognitive_functions.md   # 荣格/毕比八维模型、Naomi Quenk 8 大劣势动作库与耻感锚点
│   ├── enneagram_dynamics.md         # 里索-赫德森九型、27 副型、三元组及九型特性防火墙字典
│   └── probing_methodology.md        # 高阶工程准则、行动摩擦三公理、语义消歧与 8 大复合消歧矩阵
├── resources/                        # 报告与线索日志模板
│   ├── clue_dossier_template.md      # 后台动态线索与理论追溯档案模板
│   ├── report_template.md            # Markdown 纯文本全景档案模板
│   └── report_template.html          # 现代极简低饱和流式阅读 HTML 报告模板
├── scripts/                          # 辅助执行脚本
│   ├── scoring_engine.py             # 16 型八维功能位阶映射与副型计算引擎
│   ├── generate_report.py            # MD + HTML 双模自动渲染与时间戳归档工具
│   └── sync_plugin.ps1               # 本地源码至全局插件目录同步脚本（Windows）
└── skills/                           # 内置子 Skill 目录
    └── personality-visual-designer/  # 现代极简人文美学视觉引擎（低饱和调色盘 & LLM 手绘 SVG 规范）
```

## ⚠️ 注意事项 (Notes & Limitations)

* **建议预留充足对话时间**：为确保推导精度并穿透人格面具，完整测评通常包含 **12~18+ 轮**自然深入的对话，建议预留 15~30 分钟专注交互。
* **非临床医疗诊断声明**：本 Skill 基于荣格分析心理学与现代动态九型理论，输出内容仅供深度自我探索、认知复盘与个人发展参考，不能替代专业临床心理咨询或医学诊断。
* **多轮测试防污染与自动归档**：每次启动全新测评均会清空历史推演假设，避免旧档案污染；生成的报告与线索日志默认存放于 `outputs/`（已在 `.gitignore` 中忽略），历史批次会自动按时间戳备份至 `outputs/archive/`，不会相互覆盖丢失。

## 📄 开源协议 (License)

MIT License
