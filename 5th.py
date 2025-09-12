# 5th.py
# they are not divisible by 3,
N = int(input("Enter a number: "))
print("Numbers up to", N, "not divisible by 3, 6, or 9:")
for i in range(1, N+1):
    if i % 3 != 0 and i % 6 != 0 and i % 9 != 0:
        print(i, end=" ")
