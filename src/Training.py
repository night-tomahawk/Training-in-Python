from math import pi as число_пи
print(число_пи)
n = int(input())
print(int(n // 3))
# В гостях у бабушки
n = int(input('Укажите количество квартир на этаже '))
k = int(input('Введите номер квартиры '))
floor = k // n + bool(k % n)
floors = int(input('Введите количество этажей в доме '))
last_door = int(input('Введите номер последней квартиры на первом этаже '))
number_apartment = int(input('Введите номер квартиры бабушки '))
n = number_apartment // last_door + bool(number_apartment % last_door)
gate = n // floors + bool(floor % floors)
print(gate, (floor - floors * (gate - 1)))
