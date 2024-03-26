import calendar

# Логический тип
x, y, z = True, False, True
print(x and y or z)
x = 12
y = False
print(x or y)
x = 12
z = ''
print(x and z)
print(z and x)
x = True
y = False
print(x and y)
print(y and x)
# Год ялвяется високосным, если он кратен 4, но при этом не кратен 100, либо кратен 400
year = 2024
is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(is_leap)
print(calendar.isleap(2024))
# Выполнение условий (для записи условного оператора используются if и else)
company = 'my.com'
if 'my' in company:
    print('Найдено')
elif 'google' in company:
    print('Найдено google')
else:
    print('Ничего не найдено')
# elif заменяет "elese: if", Также можно записать условие в 1 строку.
score_1 = 5
score_2 = 0
win = 'Argentina' if score_1 > score_2 else 'Jamaica'
print(win)
