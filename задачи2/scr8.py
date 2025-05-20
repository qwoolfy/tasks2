import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_to(self, other_point):
        return math.sqrt ((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def is_on_axis(self):
        return self.x == 0 or self.y == 0
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
if __name__ == "__main__":
    point1 = Point(6, 7)
    point2 = Point(1, 2)
    
    print(f"Точка 1: {point1}")
    print(f"Точка 2: {point2}")
    
    distance = point1.distance_to(point2)
    print(f"Расстояние между точками: {distance:.2f}")
    
    print(f"Точка 1 лежит на оси x или y? {'Да' if point1.is_on_axis() else 'Нет'}")
    print(f"Точка 2 лежит на оси x или y? {'Да' if point2.is_on_axis() else 'Нет'}")
    
    point1.move(2, -1)
    print(f"Точка 1 после перемещения: {point1}")
    
    new_distance = point1.distance_to(point2)
    print(f"Новое расстояние между точками: {new_distance:.2f}")