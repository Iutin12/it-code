a = int(input("Введите число: "))
for i in range (2,a):
    if a % i == 0 :
        print("Число cоставное")
        break
    elif a >= 0:
        print('Число простое')
