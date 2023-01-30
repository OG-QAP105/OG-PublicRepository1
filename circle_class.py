"""
Создадим класс Circle (круг):
"""
class Circle:
    def __init__(self, pi, r):
        self.pi = pi
        self.r = r
    def get_area_circle(self):
        return self.pi * self.r ** 2

