#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
theme_generator.py
------------------
动态美学设计引擎：
根据受测者的 MBTI 类型与九型人格动力学，动态计算：
1. 低饱和矿物纸张调色盘；
2. 淡雅背景矢量几何/古典线条意象 (Procedural Ambient SVG)；
3. 一句话底层心智哲学格言 (Philosophical Anchor Line)。
"""

from typing import Dict, Any


# 矿物低饱和色谱预设
PALETTE_MAP = {
    # 战略系统型 (Ni / Te): 暮色青灰 + 陶土微温
    "ARCHITECT": {
        "primary": "#3E4E59",          # 暮色青灰 (Slate Indigo)
        "secondary": "#7D6B58",        # 沉稳矿褐 (Muted Bronze)
        "accent": "#9E5A48",           # 陶土微赭 (Terracotta)
        "bg_canvas": "#FAF9F5",        # 古董羊皮纸暖白
        "bg_surface": "#FFFFFF",       # 纸张纯白
        "bg_subtle": "#F4F1EA",        # 浅亚麻微灰
        "border_line": "#E5E2DA",      # 印刷铅线灰
        "text_main": "#191919",        # 油墨黑
        "text_muted": "#706E6B",       # 说明铅灰
        "badge_bg": "#EEF1F3",
    },
    # 纯逻辑探求型 (Ti / Ne): 古籍砂褐 + 冷杉灰绿
    "THEORIST": {
        "primary": "#4A584E",          # 冷杉灰绿 (Pine Sage)
        "secondary": "#7C6349",        # 古籍砂褐 (Antique Ochre)
        "accent": "#A36B42",           # 琥珀明褐
        "bg_canvas": "#FAF9F6",
        "bg_surface": "#FFFFFF",
        "bg_subtle": "#F3EFE7",
        "border_line": "#E4DFD5",
        "text_main": "#1B1A18",
        "text_muted": "#6E6B66",
        "badge_bg": "#ECEFEA",
    },
    # 纯粹理想型 (Fi / Ni): 暮紫石楠 + 浅矿苔绿
    "IDEALIST": {
        "primary": "#5A4854",          # 暮紫石楠 (Dusty Mulberry)
        "secondary": "#58695C",        # 灰苔矿绿 (Muted Sage)
        "accent": "#966540",           # 暖岩金
        "bg_canvas": "#FAF8F5",
        "bg_surface": "#FFFFFF",
        "bg_subtle": "#F5EFEF",
        "border_line": "#E6DFDE",
        "text_main": "#201D1E",
        "text_muted": "#756D70",
        "badge_bg": "#EFE8EB",
    },
    # 灵动探索型 (Ne / Se): 暖麦金浪 + 浅湖墨蓝
    "EXPLORER": {
        "primary": "#3B5A5C",          # 浅湖墨蓝 (Ocean Teal)
        "secondary": "#8C6E38",        # 暖麦金浪 (Muted Gold)
        "accent": "#A6543D",           # 砖石朱红
        "bg_canvas": "#FBF9F4",
        "bg_surface": "#FFFFFF",
        "bg_subtle": "#F6F1E6",
        "border_line": "#E8E2D4",
        "text_main": "#1C1B19",
        "text_muted": "#726E65",
        "badge_bg": "#EBF2F3",
    },
}


# 几何线条意象 SVG 生成器
def generate_metaphor_svg(svg_type: str, primary_color: str, secondary_color: str) -> str:
    """生成作为淡雅背景水印的纯线条矢量图 (SVG)"""
    if svg_type == "column_and_grid":
        # 古典石柱与透视坐标轴（象征理性架构与宏观终局）
        return f"""<svg viewBox="0 0 400 240" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <!-- 细线背景坐标网格 -->
  <line x1="20" y1="20" x2="380" y2="20" stroke="{primary_color}" stroke-opacity="0.3" stroke-width="1" stroke-dasharray="3 3"/>
  <line x1="20" y1="80" x2="380" y2="80" stroke="{primary_color}" stroke-opacity="0.3" stroke-width="1" stroke-dasharray="3 3"/>
  <line x1="20" y1="140" x2="380" y2="140" stroke="{primary_color}" stroke-opacity="0.3" stroke-width="1" stroke-dasharray="3 3"/>
  <line x1="20" y1="200" x2="380" y2="200" stroke="{primary_color}" stroke-opacity="0.3" stroke-width="1" stroke-dasharray="3 3"/>
  
  <line x1="80" y1="10" x2="80" y2="230" stroke="{primary_color}" stroke-opacity="0.3" stroke-width="1" stroke-dasharray="3 3"/>
  <line x1="200" y1="10" x2="200" y2="230" stroke="{primary_color}" stroke-opacity="0.4" stroke-width="1"/>
  <line x1="320" y1="10" x2="320" y2="230" stroke="{primary_color}" stroke-opacity="0.3" stroke-width="1" stroke-dasharray="3 3"/>

  <!-- 左侧多立克古典石柱线稿 -->
  <rect x="50" y="45" width="80" height="12" stroke="{primary_color}" stroke-width="1.2" fill="none"/>
  <line x1="45" y1="45" x2="135" y2="45" stroke="{primary_color}" stroke-width="1.5"/>
  <line x1="60" y1="57" x2="60" y2="195" stroke="{primary_color}" stroke-width="1"/>
  <line x1="72" y1="57" x2="72" y2="195" stroke="{primary_color}" stroke-width="1"/>
  <line x1="84" y1="57" x2="84" y2="195" stroke="{primary_color}" stroke-width="1.2"/>
  <line x1="96" y1="57" x2="96" y2="195" stroke="{primary_color}" stroke-width="1.2"/>
  <line x1="108" y1="57" x2="108" y2="195" stroke="{primary_color}" stroke-width="1"/>
  <line x1="120" y1="57" x2="120" y2="195" stroke="{primary_color}" stroke-width="1"/>
  <rect x="50" y="195" width="80" height="12" stroke="{primary_color}" stroke-width="1.2" fill="none"/>
  <line x1="42" y1="207" x2="138" y2="207" stroke="{primary_color}" stroke-width="1.5"/>

  <!-- 右侧几何黄金圆规曲线 -->
  <circle cx="270" cy="120" r="70" stroke="{secondary_color}" stroke-opacity="0.6" stroke-width="1"/>
  <circle cx="270" cy="120" r="45" stroke="{primary_color}" stroke-opacity="0.8" stroke-width="1.2"/>
  <circle cx="270" cy="120" r="20" stroke="{secondary_color}" stroke-opacity="0.9" stroke-width="1"/>
  <circle cx="270" cy="120" r="3" fill="{primary_color}"/>
  
  <line x1="200" y1="120" x2="340" y2="120" stroke="{primary_color}" stroke-width="1" stroke-dasharray="2 2"/>
  <line x1="270" y1="50" x2="270" y2="190" stroke="{primary_color}" stroke-width="1" stroke-dasharray="2 2"/>
  <path d="M 270,50 A 70,70 0 0,1 340,120 L 270,120 Z" fill="{secondary_color}" fill-opacity="0.12"/>
</svg>"""
    elif svg_type == "compass_astrolabe":
        # 航海星盘与经纬罗盘（探索与客观不变量）
        return f"""<svg viewBox="0 0 400 240" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <circle cx="200" cy="120" r="85" stroke="{primary_color}" stroke-opacity="0.4" stroke-width="1" stroke-dasharray="4 2"/>
  <circle cx="200" cy="120" r="70" stroke="{primary_color}" stroke-width="1.2"/>
  <circle cx="200" cy="120" r="50" stroke="{secondary_color}" stroke-width="1" stroke-opacity="0.7"/>
  <circle cx="200" cy="120" r="25" stroke="{primary_color}" stroke-width="1"/>
  <circle cx="200" cy="120" r="3" fill="{primary_color}"/>

  <line x1="200" y1="20" x2="200" y2="220" stroke="{primary_color}" stroke-width="1"/>
  <line x1="100" y1="120" x2="300" y2="120" stroke="{primary_color}" stroke-width="1"/>
  
  <line x1="140" y1="60" x2="260" y2="180" stroke="{secondary_color}" stroke-width="0.8" stroke-dasharray="3 3"/>
  <line x1="140" y1="180" x2="260" y2="60" stroke="{secondary_color}" stroke-width="0.8" stroke-dasharray="3 3"/>
  
  <!-- 八角指针微标 -->
  <polygon points="200,45 204,116 200,120 196,116" fill="{primary_color}"/>
  <polygon points="200,195 204,124 200,120 196,124" fill="{secondary_color}" fill-opacity="0.6"/>
</svg>"""
    else:
        # 几何拼贴与黄金螺线（纯粹价值与自相似演化）
        return f"""<svg viewBox="0 0 400 240" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-full">
  <rect x="60" y="30" width="80" height="80" stroke="{primary_color}" stroke-width="1" fill="{secondary_color}" fill-opacity="0.1"/>
  <rect x="140" y="30" width="130" height="80" stroke="{primary_color}" stroke-width="1" fill="none"/>
  <rect x="60" y="110" width="130" height="90" stroke="{secondary_color}" stroke-width="1" stroke-dasharray="2 2"/>
  <rect x="190" y="110" width="150" height="90" stroke="{primary_color}" stroke-width="1.2" fill="{primary_color}" fill-opacity="0.08"/>
  <path d="M 60,30 Q 140,30 140,110 T 270,110" stroke="{primary_color}" stroke-width="1.5" fill="none"/>
  <circle cx="270" cy="110" r="4" fill="{primary_color}"/>
</svg>"""


class EditorialThemeEngine:
    """
    人文出版物美学调色与意象引擎：
    - 在正式 AI 交互工作流中，意象 SVG 与心智格言优先由大模型根据具体对话自由手绘生成（不设固定模板限制）；
    - 本类提供低饱和矿物调色盘的基础映射，并为离线测试提供回退兜底。
    """

    @classmethod
    def generate_theme(
        cls,
        mbti_type: str,
        enneagram_type: str,
        custom_svg: str = None,
        custom_quote: str = None,
    ) -> Dict[str, Any]:
        mbti_upper = mbti_type.upper().strip()
        
        # 匹配大类矿物调色盘
        if any(x in mbti_upper for x in ["INTJ", "ENTJ", "INFJ"]):
            key = "ARCHITECT"
            default_svg = "column_and_grid"
            default_quote = "在喧嚣与粗糙的现实之外，筑起一座严丝合缝的真理哨所与终局沙盘。"
        elif any(x in mbti_upper for x in ["INTP", "ISTP", "ISTJ"]):
            key = "THEORIST"
            default_svg = "compass_astrolabe"
            default_quote = "万物皆有其因果咬合的齿轮，真理的自洽本身即是最大的安宁。"
        elif any(x in mbti_upper for x in ["INFP", "ISFP", "ENFJ"]):
            key = "IDEALIST"
            default_svg = "nautilus_geometric"
            default_quote = "以极度挑剔的真诚守护内心的纯粹圣殿，不向世俗虚伪妥协半分。"
        else:
            key = "EXPLORER"
            default_svg = "compass_astrolabe"
            default_quote = "生命是一场永不驻足的认知远航，可能性永远在既定的边界之外。"

        palette = PALETTE_MAP[key]

        # 优先使用 LLM 现场构思生成的 SVG 与格言，仅在未提供时使用兜底
        svg_code = custom_svg if custom_svg else generate_metaphor_svg(default_svg, palette["primary"], palette["secondary"])
        quote = custom_quote if custom_quote else default_quote

        return {
            "THEME_PRIMARY": palette["primary"],
            "THEME_SECONDARY": palette["secondary"],
            "THEME_ACCENT": palette["accent"],
            "THEME_BG_CANVAS": palette["bg_canvas"],
            "THEME_BG_SURFACE": palette["bg_surface"],
            "THEME_BG_SUBTLE": palette["bg_subtle"],
            "THEME_BORDER_LINE": palette["border_line"],
            "THEME_TEXT_MAIN": palette["text_main"],
            "THEME_TEXT_MUTED": palette["text_muted"],
            "THEME_BADGE_BG": palette["badge_bg"],
            "THEME_METAPHOR_SVG": svg_code,
            "THEME_PHILOSOPHY_QUOTE": quote,
        }


if __name__ == "__main__":
    theme = EditorialThemeEngine.generate_theme("INTJ", "5w6")
    print("=== 动态美学主题生成校验 (INTJ + 5w6) ===")
    print(f"主色: {theme['THEME_PRIMARY']}")
    print(f"格言: {theme['THEME_PHILOSOPHY_QUOTE']}")
    print(f"SVG 长度: {len(theme['THEME_METAPHOR_SVG'])} 字符")
    print("生成器运作正常。")
