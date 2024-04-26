# from random import randint
# Множества
# animals = {'cat', 'fox', 'dog', 'wolf'}
# print(animals)
# empty = set()
# animals = ['cat', 5, 'dog', 'fox']
# print(animals)
# my_set = ('a', 'b', 'c')
# print(len(my_set))
# for i in my_set:
#     print(i)
# word = 'hello'
# print(word[int(input())])
# text = 'Лень - главное достоинство программиста'
# volwes = 0
# for i in text:
#     if i in {'а', 'и', 'о'}:
#         volwes += 1
# print(volwes)
# text = 'Лень - главное достоинство программиста'
# volwes = 0
# for i in range(len(text)):
#     if text[i] in ('а', 'и', 'о'):
#         volwes += 1
# print(volwes)
# print('\u2603')
# for i in range(26):
#     print(chr(ord('A') + i), end='')
# n = 6
# num = str(n)
# print(num)
# print(type(num))
# text = 'hello, world'
# print(text[0:5])
# print(text[:-6])
# text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# print(text[::-1])
# s = ' one two three'
# print(s.split())
# print(type(s.split()))
# s1 = ['раз', 'два', 'три']
# s2 = ' '.join(s1)
# # print(type(' '.join(s1)))
# print(s + s2)
# Списки
# empty = []
# empty = list()
# print(empty)
# my_list = [None] *8
# print(my_list)
# a = ['list', 'set', 'dict', 'tuple']
# b = [
#     ['Anna', 10.5],
#     ['Alex', 5.2]
# ]
# print(len(b))
# print(a[:-1])
# print('list' in a)
# my_list = list(range(10))
# print(my_list)
# my_list.append('3')
# print(my_list)
# my_list.extend(['hello', 'world'])
# my_list = list(range(18))
# print(my_list)
# print(min(my_list))
# print(max(my_list))
# print(sum(my_list))
# n = []
# for i in range(10):
#     n.append(randint(1,30))
# print(n)
# a = sorted(n, reverse=True)
# print(a)
# a = n.sort()
# print(n)
# Кортежи - неизменяемые списки
# empty = ()
# empty = tuple()
# print(empty)
# a = (1, 2, 30)
# print(a[0])
# b = ([],[])
# b[0].append(0)
# print(b)
# s = []
# for i in range(10):
#     if i % 2 == 0:
#         s.append(i ** 2)
# print(s)
# # Списочное выражение
# s = [i ** 2 for i in range(10) if i % 2 == 0]
# print(s)
# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(a)
# n = 5
# b = []
# for i in range(n):
#     row = [int(x) for x in input().split()]
#     b.append(row)
# print(b)
# import pandas as pd
#
# # Создаем пример датафрейма
# df = pd.DataFrame({'A': ['apple', 'banana', 'cherry', 'date', 'elderberry'],
#                    'B': [5, 10, 3, 8, 4]})
#
# # Функция для определения условий на основе значений столбца 'B'
# def check_fruit_length(word):
#     if len(word) > 5:
#         return 'Long fruit'
#     else:
#         return 'Short fruit'
#
# # Добавляем новый столбец 'C', зависящий от значений столбца 'A'
# df['C'] = df['A'].apply(check_fruit_length)
#
# print(df)
import pandas as pd

# Создание примера датафрейма
data = {'Имя': ['Иван', 'Мария', 'Петр'],
        'Возраст': [25, 30, 22],
        'Город': ['Москва', 'Санкт-Петербург', 'Казань']}
df = pd.DataFrame(data)

# Форматированный вывод таблицы из датафрейма
print(df.to_string(index=False))