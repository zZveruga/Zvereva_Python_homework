import math


def square(side):
   return math.ceil(side * side)


side = int(input("Сторона квадрата: "))
print(f"Площадь квадрата: {square(side)}")
