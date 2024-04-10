# import pyowm
# owm = pyowm.OWM('603014a288b8718af660386383703b6b')
# mgr = owm.weather_manager()
# place = input("В каком городе/стране?: ")
# observation = mgr.weather_at_place(place)
# w = observation.weather
# temperature = w.temperature('celsius')['temp']
# humidity = w.humidity
# status = w.status
# print(w)
# Калькулятор для чайников v.1
# what = input("Что делаем?(+,-): ")
# a = float(input('Введи первое число: '))
# b = float(input('Введи второе число: '))
# if what == '+':
#     c = a + b
#     print('Результат: ' + str(c))
# elif what == '-':
#     c = a - b
#     print('Результат: ' + str(c))
# else:
#     print('Выбрана неверная операция!')
# Калькулятор для чайников v.2
# from colorama import init, Fore, Back, Style
# init()
# print(Fore.BLACK)
# print(Back.GREEN)
# what = input("Что делаем?(+,-,*,/): ")
# print(Back.CYAN)
# a = float(input('Введи первое число: '))
# b = float(input('Введи второе число: '))
# print(Back.YELLOW)
# if what == '+':
#     c = a + b
#     print('Результат: ' + str(c))
# elif what == '-':
#     c = a - b
#     print('Результат: ' + str(c))
# elif what == '*':
#     c = a * b
#     print('Результат: ' + str(c))
# elif what == '/':
#     c = a / b
#     print('Результат: ' + str(c))
# else:
#     print('Выбрана неверная операция!')
