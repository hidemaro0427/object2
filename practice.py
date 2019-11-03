class Circle:
    def __init__(self, radius):
        self.exercise_rate = 3.14
        self.radius = radius

    def area(self):
        self.area = self.radius ** 2 * self.exercise_rate
        return self.area


# Todo 表示できない
circle1 = Circle(radius=1)
print(circle1.area)  # 3.14
# print(circle1.perimeter())  # 6.28
