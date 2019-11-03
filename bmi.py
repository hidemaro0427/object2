"""
class BMI:
    関連しそうな属性
        - 身長
        - 体重
        - BMIという値そのもの
    ルール:
        - 10以上40以下<-- 常識的な範囲
        - 表示する時は、少数第2位まで
            - ex: 23.678 -> 23.67
            - ex: 23.671 -> 23.67
    できること:
        - ???
"""

# クラス名はUpperCamelCaseが普通
class BMI:
    def __init__(self, height, weight):
        self.value = weight / (height ** 2)

        if not (10 <= self.value <= 0):
            raise ValueError('BMIが正常値の範囲を超えています')

    def __str__(self):
        return f'{self.value:.2f}'


hikibi_bmi = BMI(height=1.80, weight=67.0)
print(hikibi_bmi)

ohira_bmi = BMI(height=1.78, weight=75.0)
print(ohira_bmi)

yabai_bmi = BMI(height=1.78, weight=75000.0)
