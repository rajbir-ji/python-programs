import math
# Circle
r = float(input("Enter radius of circle: "))
circle_area = math.pi * r * r
print("Area of Circle =", circle_area)
# Rectangle
l = float(input("\nEnter length of rectangle: "))
w = float(input("Enter width of rectangle: "))
rectangle_area = l * w
print("Area of Rectangle =", rectangle_area) 
# Triangle
b = float(input("\nEnter base of triangle: "))
h = float(input("Enter height of triangle: "))
triangle_area = 0.5 * b * h
print("Area of Triangle =", triangle_area)
# Square
s = float(input("\nEnter side of square: "))
square_area = s * s
print("Area of Square =", square_area)
# Trapezoid
a = float(input("\nEnter first base of trapezoid: "))
b = float(input("Enter second base of trapezoid: "))
h = float(input("Enter height of trapezoid: "))
trapezoid_area = 0.5 * (a + b) * h
print("Area of Trapezoid =", trapezoid_area)
# Parallelogram
bp = float(input("\nEnter base of parallelogram: "))
hp = float(input("Enter height of parallelogram: "))
parallelogram_area = bp * hp
print("Area of Parallelogram =", parallelogram_area)
