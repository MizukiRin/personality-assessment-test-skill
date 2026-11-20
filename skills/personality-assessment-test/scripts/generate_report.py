#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_report.py
------------------
结合 resources/report_template.md 与 resources/report_template.html，
同时支持调用 visual-designer 美学引擎生成现代极简低饱和纸质排印风格 HTML 档案。
"""

import os
import sys
from datetime import datetime

# 尝试连接视觉设计子 Skill
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
VISUAL_DESIGNER_DIR = os.path.join(BASE_DIR, "skills", "personality-visual-designer")

if os.path.exists(VISUAL_DESIGNER_DIR):
    sys.path.append(os.path.join(VISUAL_DESIGNER_DIR, "scripts"))
    try:
        from theme_generator import EditorialThemeEngine
    except ImportError:
        EditorialThemeEngine = None
else:
    EditorialThemeEngine = None


DEFAULT_PARAMS = {
    # 基础画像与类型
    "USER_ALIAS": "用户昵称",
    "ASSESSMENT_DATE": datetime.now().strftime("%Y-%m-%d"),
    "MBTI_TYPE": "INTJ (建筑师 / 战略家)",
    "ENNEAGRAM_PROFILE": "5w6 (系统防灾理智观察者)",
    "TRITYPE": "5-8-3",
    "INSTINCT_STACK": "sp/sx (so-blind)",

    # 现代极简低饱和调色盘 (矿物纸质排印风格)
    "THEME_PRIMARY": "#3E4E59",          # 暮色青灰 (Slate Indigo)
    "THEME_SECONDARY": "#7D6B58",        # 沉稳矿褐 (Muted Bronze)
    "THEME_ACCENT": "#9E5A48",           # 陶土微赭 (Terracotta)
    "THEME_BG_CANVAS": "#FAF9F5",        # 羊皮纸暖白底色
    "THEME_BG_SURFACE": "#FFFFFF",       # 卡片洁白底色
    "THEME_BG_SUBTLE": "#F4F1EA",        # 浅亚麻灰微底
    "THEME_BORDER_LINE": "#E5E2DA",      # 极简细边框线
    "THEME_TEXT_MAIN": "#191919",        # 油墨黑
    "THEME_TEXT_MUTED": "#706E6B",       # 说明铅灰
    "THEME_BADGE_BG": "#EEF1F3",
    "THEME_PHILOSOPHY_QUOTE": "在喧嚣与粗糙的现实之外，筑起一座严丝合缝的真理哨所与终局沙盘。",
    "THEME_METAPHOR_SVG": "",            # 自动注入几何线条意象

    # 八维功能栈
    "DOMINANT_FUNC": "Ni (内倾直觉)",
    "DOM_DESC": "终局宏观洞察、底层因果、顶层沙盘收敛",
    "AUXILIARY_FUNC": "Te (外倾思考)",
    "AUX_DESC": "系统规则架构、SOP防灾排雷、实效闭环落地",
    "TERTIARY_FUNC": "Fi (内倾情感)",
    "TERT_DESC": "永恒之童、深层纯粹价值观与安全护城河",
    "INFERIOR_FUNC": "Se (外倾感觉)",
    "INF_DESC": "阿尼玛劣势体验、物理杂事启动高摩擦力",
    "TRICKSTER_FUNC": "Fe (外倾情感)",
    "TRICK_DESC": "第七盲区、蔑视虚伪世俗礼节、人情电量快速断电",
    "INTEGRATION_DESC": "向 8 号健康整合（勇于亮剑、捍卫权责利边界）",
    "INSTINCT_DESC": "自保城堡主 + 挑剔纯粹的灵魂探寻者",
    "TRITYPE_DEFENSE_HIERARCHY": "5 (抽离观察防守) ➔ 8 (侵犯时亮剑自卫) ➔ 3 (硬核胜任力自尊)",

    # 八维深度机制
    "DOM_MECHANISM": "本能捕捉事物背后隐匿的底层架构，在脑海预先跑通多分支沙盘，只向终局最优解效忠。",
    "DOM_EXPERIENCE": "‘我一眼就能看到这个架构长远一定会暴雷’的因果直觉。",
    "AUX_MECHANISM": "思维必须落在纸笔、文档、流程图与跑实验等客观载体上，排斥空中楼阁。",
    "AUX_REALITY_ANCHOR": "通过梳理 SOP 与极端实用剪裁（ROI 最优）驱动项目安全交付。",
    "TERT_SANCTUARY": "对内保持极度挑剔但纯粹干净的情感圣殿，对外绝不滥用同情。",
    "INF_DAILY_FRICTION": "在面对填表、打卡、收拾物理房间等感官杂物时，存在高强度的启动阻抗与心智耗竭。",
    "INF_GRIP_BEHAVIOR": "在长期压力极限崩溃时，出现暴饮暴食、过度即时感官放纵等代偿反应。",
    "TRICKSTER_BEHAVIOR": "面对敬酒、人情寒暄等低信噪比应酬感到生理性荒谬与疲倦。",

    # 九型动力机制
    "ENERGY_MODEL": "电量守恒算法：日常处于极低功耗待机，战时化身单点聚焦的轨道炮。",
    "DOM_INSTINCT_ANALYSIS": "严格界定物理空间与个人精力配额，严防精力被外部无端索取。",
    "SEC_INSTINCT_ANALYSIS": "对极少数高度信赖的纯粹灵魂保留绝对深度的情感依恋。",
    "BLIND_INSTINCT_ANALYSIS": "对群体氛围、人情客套与组织归属感具有天然的无痕脱敏与冷感。",
    "TRITYPE_LEVEL_1": "面对外部问题先抽离退回城堡，调动因果逻辑与认知储备评估全局。",
    "TRITYPE_LEVEL_2": "当专业主权或边界被公然踩踏时，调用 8 号硬核力量正面刚纠偏。",
    "TRITYPE_LEVEL_3": "深层焦虑来源于对无能与随大流的恐惧，誓以硬核实力捍卫自主尊严。",

    # 复合特质与跨型号辨析
    "COMPOSITE_TYPICAL_TRAITS": "外表沉静抽离、极度重视个人主权边界，面对复杂课题时展现出惊人的专注力与系统穿透力。",
    "COMPOSITE_DECISION_STYLE": "目标明确时迅速排定优先级、寻找全局最优解；没有明确目标时呈现节能待机状态。",
    "COMPOSITE_RELATIONAL_STYLE": "商务与工作沟通极其高效客观、讲求权责利清晰；对虚伪寒暄与人情世故极度不耐烦。",
    "CROSS_ENNEAGRAM_DIFF_A": "若搭配 1 号（1w9）：则表现为高度苛求完美的教条主义与道德秩序，而非 5 号的节能与因果闭环。",
    "CROSS_ENNEAGRAM_DIFF_B": "若搭配 3 号（3w4）：则表现为强烈的个人外显野心与商业光环追求，而非 5 号的隐退观察者特质。",
    "FIT_RATIONALE": "自保 5 号的能量吊桥法则与 6 号侧翼的防灾预警，完全解释了受测者的能耗节制与高标准交付动力。",

    # 擅长领域与跃升指南
    "CORE_ADVANTAGE_DOMAINS": "顶层业务架构设计、系统规则与流程制定、前沿复杂技术攻坚、单兵深度研究与方案裁决。",
    "OPTIMAL_WORKING_MODE": "独立负责完整模块（Owner 机制）、异步沟通为主、权责清晰、高信噪比的信息输入环境。",
    "BLINDSPOT_AVOIDANCE": "警惕因过度追求闭环推导而陷入启动拖延高墙；在人际沟通中避免将客观事实直说转化为攻击感。",
    "INFERIOR_DEVELOPMENT": "将劣势 Se 转化为主动的感官放松（如自然散步、高审美体验），以微习惯跨越琐事启动高阻抗。",
    "ENERGY_PRESERVATION_STRATEGY": "建立不可动摇的私人能量安全区，不必为社交钝感产生任何道德负罪感。",
    "INTEGRATION_PRACTICE": "在边界受阻时主动调用 8 号的坦率力量直接亮剑，减少事后内耗与概念反刍。"
}


def render_file(template_path: str, output_path: str, params: dict):
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"未找到模板文件: {template_path}")

    with open(template_path, "r", encoding="utf-8") as f:
        content = f.read()

    for key, value in params.items():
        placeholder = "{" + key + "}"
        content = content.replace(placeholder, str(value))

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[OK] 成功生成: {output_path}")


def generate_reports(output_dir: str = None, params: dict = None, auto_archive: bool = True):
    if params is None:
        params = dict(DEFAULT_PARAMS)

    # 尝试调用视觉子 Skill 计算动态主题（若用户/LLM已提供专属 SVG 或格言，严格优先使用）
    if EditorialThemeEngine:
        visual_data = EditorialThemeEngine.generate_theme(
            params.get("MBTI_TYPE", "INTJ"),
            params.get("ENNEAGRAM_PROFILE", "5w6"),
            custom_svg=params.get("THEME_METAPHOR_SVG"),
            custom_quote=params.get("THEME_PHILOSOPHY_QUOTE"),
        )
        params.update(visual_data)

    if output_dir is None:
        output_dir = os.path.join(BASE_DIR, "outputs")
    os.makedirs(output_dir, exist_ok=True)

    md_tpl = os.path.join(BASE_DIR, "resources", "report_template.md")
    html_tpl = os.path.join(BASE_DIR, "resources", "report_template.html")

    # 1. 始终生成/更新 outputs/ 下的固定文件（作为“最新报告”入口，方便用户即开即看）
    md_out = os.path.join(output_dir, "personality_profile.md")
    html_out = os.path.join(output_dir, "personality_profile.html")

    render_file(md_tpl, md_out, params)
    render_file(html_tpl, html_out, params)

    # 2. 自动归档：同步在 outputs/archive/ 保存带时间戳与受测者代号的历史独立副本
    if auto_archive:
        import shutil
        timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        alias_clean = "".join(c for c in str(params.get("USER_ALIAS", "user")) if c.isalnum() or c in ("-", "_")).strip()
        if not alias_clean:
            alias_clean = "profile"
        archive_dir = os.path.join(output_dir, "archive", f"{timestamp_str}_{alias_clean}")
        os.makedirs(archive_dir, exist_ok=True)

        render_file(md_tpl, os.path.join(archive_dir, "personality_profile.md"), params)
        render_file(html_tpl, os.path.join(archive_dir, "personality_profile.html"), params)

        # 若当前存在本次的线索追溯档案，也一并安全镜像归档
        clue_src = os.path.join(output_dir, "clue_tracking_dossier.md")
        if os.path.exists(clue_src):
            shutil.copy2(clue_src, os.path.join(archive_dir, "clue_tracking_dossier.md"))

        print(f"[Archive] 本次测评全景档案已安全归档至: {archive_dir}")


if __name__ == "__main__":
    generate_reports()
    print("双模报告生成完毕，请打开 outputs/personality_profile.html 体验新设计！")
