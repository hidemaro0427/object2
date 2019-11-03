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
        self.height = height
        self.weight = weight

    def calculatebmi_bmi(self):
        return self.weight / (self.height ** 2)


# BMIクラスのインスタンス化
hibiki_bmi = BMI(height=1.80, weight=67.0)
noriya_bmi = BMI(height=1.78, weight=75.0)

print(hibiki_bmi.height, hibiki_bmi.weight)
print(hibiki_bmi.calculatebmi_bmi())
