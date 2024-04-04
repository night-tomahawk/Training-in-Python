# Цикл while
# n = int(input())
# i = 1
# while i <= n:
#     print(i)
#     i += 1
# now = int(input())
# now_min = now
# while now != 0:
#     if now < now_min:
#         now_min = now
#     now = int(input())
# print(now_min)
# count = 0
# num = int(input())
# while num != 0:
#     if num % 10 == 1 and num % 4 == 0:
#         count += 1
#         num = int(input())
#         print(count)
# функция while используется когда цикл может повторяться неограниченное количество раз,
# 'FOR' когда сам задаешь количество повторений
# num = int(input())
# while num > 0:
#     print(num % 10)
#     num //= 10
# n = int(input())
# for i in range(n):
#     print(i)
# # Определить сумму целых чисел от 0 до 101 с шагом 5
# n = 0
# for i in range(100, 0, -1):
#     n += i
# print(n)
# i = 1
# while True:
#     print(i, end='')
#     i = i + 1
#     if i > 100:
#         continue
# n = int(input())
# for i in range(3, n, 2):
#     count = 0
#     for j in range (2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             count += 1
#             break
#     if count == 0:
#         print(i)
# x = -9
# print(abs(x))
# print(round(2.6))
# word = input()
# lenght = len(word)
# print(lenght)
# a = 10
# print(dir(a))
# print("ООО Медовый Гексагон")
# print("Мёд липовый", end=" ")
# print(1, end="шт ")
# print(1250, end="р")
# print("\nCумма", 1250, end="р")
# print("\nСпасибо за покупку!")
# def print_check(honey_positions):
#     sum = 0  # переменная для накопления общей суммы
#     print("ООО Медовый Гексагон\n")
#     # в цикле будем выводить название, количество и цену
#     for honey in honey_positions:
#         name = honey[0]
#         amount = honey[1]
#         price = honey[2]
#         print(f"{name} ({amount} шт.) - {price} руб.")
#         sum += amount * price  # здесь же будем считать ещё и общую сумму
#     print(f"\nИтого: {sum} руб.")
#     print("Спасибо за покупку!")
# honey_positions = [
#     ("Мёд липовый", 8, 1250),
#     ("Мёд цветочный", 7, 1000),
#     ("Мёд гречишный", 6, 1300),
#     ("Донниковый мёд", 1, 1750),
#     ("Малиновый мёд", 10, 2000),
# ]
# print_check(honey_positions)
def data_Assasins(log, pas):
    print('login:', log)
    print('password:', pas)
data_Assasins('дай пожалуйста', 'данные для входа:)')
