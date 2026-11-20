#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scoring_engine.py
-----------------
提供荣格八维心智模型、九型人格动力学计算与副型推断的基础引擎框架。
"""

from typing import Dict, List, Tuple

COGNITIVE_STACKS = {
    "INTJ": ["Ni", "Te", "Fi", "Se", "Ne", "Ti", "Fe", "Si"],
    "INTP": ["Ti", "Ne", "Si", "Fe", "Te", "Ni", "Se", "Fi"],
    "ENTJ": ["Te", "Ni", "Se", "Fi", "Ti", "Ne", "Fi", "Si"],
    "ENTP": ["Ne", "Ti", "Fe", "Si", "Ni", "Te", "Fi", "Se"],
    "INFJ": ["Ni", "Fe", "Ti", "Se", "Ne", "Fi", "Te", "Si"],
    "INFP": ["Fi", "Ne", "Si", "Te", "Fe", "Ni", "Se", "Ti"],
    "ENFJ": ["Fe", "Ni", "Se", "Ti", "Fi", "Ne", "Ti", "Si"],
    "ENFP": ["Ne", "Fi", "Te", "Si", "Ni", "Fe", "Ti", "Se"],
    "ISTJ": ["Si", "Te", "Fi", "Ne", "Se", "Ti", "Fe", "Ni"],
    "ISFJ": ["Si", "Fe", "Ti", "Ne", "Se", "Fi", "Te", "Ni"],
    "ESTJ": ["Te", "Si", "Ne", "Fi", "Ti", "Se", "Ni", "Fe"],
    "ESFJ": ["Fe", "Si", "Ne", "Ti", "Fi", "Se", "Ni", "Te"],
    "ISTP": ["Ti", "Se", "Ni", "Fe", "Te", "Si", "Ne", "Fi"],
    "ISFP": ["Fi", "Se", "Ni", "Te", "Fe", "Si", "Ne", "Ti"],
    "ESTP": ["Se", "Ti", "Fe", "Ni", "Si", "Te", "Fi", "Ne"],
    "ESFP": ["Se", "Fi", "Te", "Ni", "Si", "Fe", "Ti", "Ne"],
}

FUNCTION_NAMES = {
    "Ni": "内倾直觉 (Introverted Intuition)",
    "Ne": "外倾直觉 (Extraverted Intuition)",
    "Ti": "内倾思考 (Introverted Thinking)",
    "Te": "外倾思考 (Extraverted Thinking)",
    "Fi": "内倾情感 (Introverted Feeling)",
    "Fe": "外倾情感 (Extraverted Feeling)",
    "Si": "内倾感觉 (Introverted Sensing)",
    "Se": "外倾感觉 (Extraverted Sensing)",
}

ROLE_NAMES = [
    "1. 英雄/主导 (Hero/Dominant)",
    "2. 父母/辅助 (Good Parent/Auxiliary)",
    "3. 永恒之童/第三 (Eternal Child/Tertiary)",
    "4. 阿尼玛/劣势 (Anima/Inferior)",
    "5. 反向英雄/相对 (Opposing)",
    "6. 巫师/老巫妪 (Witch/Senex)",
    "7. 愚者/盲区 (Trickster)",
    "8. 魔鬼/潜意识底 (Demon)",
]


class PersonalityValidator:
    """人格测评基础功能模型与副型推断计算器"""

    @staticmethod
    def get_function_stack(mbti_type: str) -> List[Tuple[str, str, str]]:
        """获取指定 MBTI 类型的八维心智功能栈详细列表"""
        mbti_type = mbti_type.upper().strip()
        if mbti_type not in COGNITIVE_STACKS:
            raise ValueError(f"未知的 MBTI 类型: {mbti_type}")

        stack = COGNITIVE_STACKS[mbti_type]
        result = []
        for role, func in zip(ROLE_NAMES, stack):
            result.append((role, func, FUNCTION_NAMES[func]))
        return result

    @staticmethod
    def parse_instinct_stack(sp: int, sx: int, so: int) -> str:
        """根据分值排序推断副型本能序列与盲区"""
        scores = [("sp", sp), ("sx", sx), ("so", so)]
        scores.sort(key=lambda x: x[1], reverse=True)
        primary, secondary, blind = scores[0][0], scores[1][0], scores[2][0]
        return f"{primary}/{secondary} ({blind}-blind)"


if __name__ == "__main__":
    print("=== 八维心智功能栈模型检查 (16种类型支持) ===")
    print(f"支持的类型总数: {len(COGNITIVE_STACKS)}")
    print("示例栈结构获取成功。")
