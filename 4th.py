import math
# Input values
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))
# Discriminant
d = b**2 - 4*a*c
# Roots
if d >= 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("Root 1 =", root1)
    print("Root 2 =", root2)
else:
    print("Roots are imaginary (no real roots).")
