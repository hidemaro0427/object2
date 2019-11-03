class Circle:
    def __init__(self, radius):
        self.exercise_rate = 3.14
        self.radius = radius
        self.area = self.radius ** 2 * self.exercise_rate

    def area(self):
        return self.area



circle1 = Circle(radius=1)
print(circle1.area)  # 3.14
# print(circle1.perimeter())  # 6.28
