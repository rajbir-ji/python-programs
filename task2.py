# 1. Check Age for Voting
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
# 2. Check Range
num = int(input("Enter a number: "))
if 1 <= num <= 100:
    print("Valid")
else:
    print("Invalid")
# 3. Leap Year Check
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
# 4. Grade System
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")