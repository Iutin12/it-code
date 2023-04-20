n = int(input("Введите число: "))

a = 0
b = 1

while n > 2:
    a, b = b, a+b
    n = n - 1

print(b)