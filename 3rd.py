import math
# Cube
a = float(input("Enter side of cube: "))
cube_volume = a ** 3
print("Volume of Cube =", cube_volume)
# Cylinder
r = float(input("\nEnter radius of cylinder: "))
h = float(input("Enter height of cylinder: "))
cylinder_volume = math.pi * r**2 * h
print("Volume of Cylinder =", cylinder_volume)
# Cone
r = float(input("\nEnter radius of cone: "))
h = float(input("Enter height of cone: "))
cone_volume = (1/3) * math.pi * r**2 * h
print("Volume of Cone =", cone_volume)
# Sphere
r = float(input("\nEnter radius of sphere: "))
sphere_volume = (4/3) * math.pi * r**3
print("Volume of Sphere =", sphere_volume)
