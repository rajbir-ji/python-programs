a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a == b or b == c or a == c:
    print("The triangle is Isosceles.")
else:
    print("The triangle is not Isosceles.")
