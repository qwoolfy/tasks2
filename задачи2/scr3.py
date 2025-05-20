class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def is_triangle(self):
        if not all(isinstance(side, (int, float)) for side in [self.a, self.b, self.c]):
            return 'Нужно вводить только числа!'
        if any(side <= 0 for side in [self.a, self.b, self.c]):
            return 'С отрицательными числами ничего не выйдет!'
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            return 'Ура, можно построить треугольник!'
        else:
            return 'Жаль, но из этого треугольник не сделать.'
check = TriangleChecker(3, 4, 5)
print(check.is_triangle())

check = TriangleChecker(1, 1, 1)
print(check.is_triangle())

check = TriangleChecker(-3, 4, 5)
print(check.is_triangle())

check = TriangleChecker("a", 4, 5)
print(check.is_triangle())