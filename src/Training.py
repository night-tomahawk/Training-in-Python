n = int(input())
print(int(n // 3))
# В гостях у бабушки
n = int(input('Укажите количество квартир на этаже '))
k = int(input('Введите номер квартиры '))
floor = k // n + bool(k % n)
print(floor)
