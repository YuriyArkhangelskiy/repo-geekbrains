print("Print number")
n = int(input())
b = 0
while n != 0:
    a = n % 10
    if a >= b:
        b = a
    n = n // 10
print(b)
