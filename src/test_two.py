num = 13
print(num)
num = 0
print(num)
num = -10
print(num)
num = 100_000_000
print(num)
print(type(num))
num = 13.4
print(num)
print(type(num))
num = 100_032.000_001
print(num)
num = 1.5e2
print(num)
num = 150.2
print(type(num))
num = int(num)
print(type(num))
print(num)
num = float(num)
print(type(num))
print(num)
num = 14 + 1j
print(type(num))
print(num.real)
print(num.imag)
#Дано четырехзначное число, найти сумму крайних цифр числа
num = int(input())
print(num % 10 + num // 1000)
#Проверить является ли введеное число степенью двойки. Если да, то вывести 0, в противном случае вывести любое число.
n = int(input())
print(n & (n-1))
#Найти расстояние между двумя точками в декартовых координатах.
x1, y1 = 0, 0
x2 = 3
y2 = 4
distance = ((x2-x1)**2+(y2-y1)**2)**0.5
print(distance)
