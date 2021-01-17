print("Type starting segment")
a = int(input())
print("Type desired distance")
b = int(input())
n = 0
while a < b:
    n = n + 1
    a = a * 1.1
print("You need", n, "days")
