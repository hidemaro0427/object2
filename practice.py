class Circle:
    def __init__(self, radius):
        self.exercise_rate = 3.14
        self.radius = radius
        self.area = self.radius ** 2 * self.exercise_rate

        self.perimeter = (self.radius) * 2 * self.exercise_rate

    def area(self):
        return self.area

    def perimeter(self):
        return self.perimeter

circle1 = Circle(radius=1)
print(circle1.area)
print(circle1.perimeter)
