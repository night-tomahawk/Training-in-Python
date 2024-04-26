import pandas as pd
# import numpy as np
# y = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# print(y)
# x = pd.Series(np.random.randint(-5, 6, 10), index=list('abcdefghij'))
# print(x)
# data = {i: np.random.randint(10) for i in 'abcdefghij'}
# z = pd.Series(data)
# z = pd.Series(data, index=list('facdbxyz'))
# print(z)
# s = pd.Series([1, 2, 3, 4])
# print(s)
# print(s.index)
# print(y.index)
# x = pd.Series(np.random.randint(-5, 6, 12), index=['a']*6 + ['b']*6)
# print(x)
# print(x.index)
# d = {'Moscow': 1000, 'Lonod': 300, 'Prague': None}
# cities = pd.Series(d)
# print(cities)
# data = {i: np.random.randint(10) for i in 'abcdefghij'}
# z = pd.Series(data)
# z = pd.Series(data, index=list('facdbxyz'))
# print(z)
# z = pd.Series(777, index=list('abcdefghij'))
# print(z)
# x = pd.Series(np.random.randint(-5, 6, 10), index=list('abcdefghij'))
# print(x[::2])
# d = {'Moscow': 1000, 'London': 300, 'Prague': None}
# cities = pd.Series(d)
# print(cities[['Moscow', 'London']])
# print('London' in cities)
# print(cities.keys())
# print(cities.values)
# print(cities[cities > 500])
# cities['Moscow'] = 100
# print(cities)
# cities[cities < 1000] = 3
# print(cities)
# print(cities[cities.isnull()])
# print(cities[cities.notnull()])
# s1 = pd.Series(np.arange(5), index=list('abcde'))
# s2 = pd.Series(np.arange(5, 10), index=list('acexy'))
# print(s1,s2)
# print(s1 + s2)
titanic = pd.read_csv('D:/programing/python-base/homework.csv', index_col=0)
print(titanic)
# # Первые 10 строк
# print(titanic.head(10))
# # Крайние 10 строк
# print(titanic.tail(10))
# # Кол-во строк и столбцов (размер таблицы)
# print(titanic.shape)
# # Названия столбцов
# print(titanic.columns)
# print(titanic.dtypes)
# # Вывод данных конкретных столбцов
# print(titanic[['Survived', 'Pclass']].head())
# titanic = pd.read_csv('titanic.csv', nrows=5, usecols=['Name', 'Survived'])
# print(titanic)
# значения толбцов для конкретной строки (обращение по индексам)
# print(titanic.iloc[-1])
# print(titanic.iloc[-1, 2])
# значения толбцов для конкретной строки (обращение по имени)
# print(titanic.loc[891, 'Name'])
# print(titanic.iloc[0:6, 2])
# print(titanic.loc[0:6, 'Pclass':'Age'])
# print(titanic[titanic['Age'] >=60])
# print(titanic[(titanic['Age'] >=60) & (titanic['Sex']=='female')])
# print(titanic[titanic['Age'].isnull()])
# print(titanic[titanic['Age'].between(50,60)])
# print(titanic['Age'].head())
# Выделить каждого десятого по имени и статусу
# print(titanic.iloc[::10][['Name', 'Survived']])
# Замена данных Борт посадки поменяем с англ. на рус.
# print(titanic['Embarked'].replace('S', 'Сс').to_frame())
# замена имени столбца или строки "rename"
# print(titanic.describe())
# print(titanic.describe(include=[np.object]))
# print(titanic['Embarked'].unique())
import pandas as pd
import pandas as pd

# Создание примера датафрейма
df = pd.DataFrame({'Количество': [3, 6, 8, 2, 10]})

# Добавление нового столбца
df['Статус'] = df['Количество'].apply(lambda x: 'Больше 5' if x > 5 else 'Меньше или равно 5')

print(df)

# data = [
#     ['Other Theft', 2003, 5, 12, 16, 15, 'Strathcona', 49.269802, -123.083763],
#     ['Other Theft', 2003, 5, 7, 15, 20, 'Strathcona', 49.269802, -123.083763],
#     ['Other Theft', 2003, 4, 23, 16, 40, 'Strathcona', 49.269802, -123.083763],
#     ['Other Theft', 2003, 4, 20, 11, 15, 'Strathcona', 49.269802, -123.083763],
#     ['Other Theft', 2003, 4, 12, 17, 45, 'Strathcona', 49.269802, -123.083763],
#     ['Other Theft', 2003, 3, 26, 20, 45, 'Strathcona', 49.269802, -123.083763],
#     ['Offence Against a Person', 2015, 8, 11, 'unknown', 'unknown', 'unknown', 0.000000, 0.000000],
#     ['Break and Enter Residential/Other', 2003, 3, 10, 12, 0, 'Kerrisdale', 49.228051, -123.146610],
#     ['Mischief', 2003, 6, 28, 4, 13, 'Dunbar-Southlands', 49.255559, -123.193725],
#     ['Mischief', 2017, 3, 26, 23, 0, 'Sunset', 49.21431483, -123.101945],
#     ['Other Theft', 2003, 2, 16, 9, 2, 'Strathcona', 49.269802, -123.083763],
#     ['Break and Enter Residential/Other', 2003, 7, 9, 18, 15, 'Grandview-Woodland', 49.267734, -123.067654],
#     ['Other Theft', 2003, 1, 31, 19, 45, 'Strathcona', 49.269802, -123.083763],
#     ['Mischief', 2003, 9, 27, 1, 0, 'Dunbar-Southlands', 49.253762, -123.194407],
#     ['Offence Against a Person', 2017, 1, 24, 'unknown', 'unknown', 'unknown', 0.000000, 0.000000],
#     ['Break and Enter Residential/Other', 2003, 4, 19, 18, 0, 'Grandview-Woodland', 49.267814, -123.067441],
#     ['Break and Enter Residential/Other', 2003, 9, 24, 18, 30, 'Grandview-Woodland', 49.267731, -123.067302],
#     ['Break and Enter Residential/Other', 2003, 11, 5, 8, 12, 'Sunset', 49.226430, -123.085283],
#     ['Break and Enter Commercial', 2003, 9, 26, 2, 30, 'West End', 49.284715, -123.122824],
#     ['Break and Enter Residential/Other', 2003, 10, 21, 10, 0, 'Grandview-Woodland', 49.267811, -123.067089],
#     ['Other Theft', 2003, 1, 25, 12, 30, 'Strathcona', 49.269802, -123.083763],
#     ['Offence Against a Person', 2003, 2, 12, 'unknown', 'unknown', 'unknown', 0.000000, 0.000000],
#     ['Other Theft', 2003, 1, 9, 6, 45, 'Strathcona', 49.269802, -123.083763],
#     ['Offence Against a Person', 2008, 2, 6, 'unknown', 'unknown', 'unknown', 0.000000, 0.000000],
# ]
# # Bool = ['1';]
# df = pd.DataFrame(data)
# # print(df)
# # df = df.rename(
# #    columns={'0': 'TYPE', '1': 'YEAR', '2': 'MONTH', '3': 'DAY', '4': 'HOUR', '5': 'MINUTE', '6': 'NEIGHBOURHOOD',
# #             '7': 'Latitude', '8': 'Longitude'}
# # )
# # print(df.shape)
# # for row in data:
# #    print('{: <33} | {: <2} '.format(*row))
# import pandas as pd
#
# homework = pd.read_csv('D:/programing/python-base/homework.csv', index_col=0)
# homework_lost = {    homework.loc[homework['HOUR'] = unknown, 'Bool'] = '0'
#     homework.loc[homework['HOUR'] != unknown, 'Bool'] = '1'
# }
# homework['Bool'] = homework_lost
# print(homework)
# for row in homework_sorted:
#     print('{: <7} | {: <7}'.format(*row))
# separator = '|'
# separated_string = homework_sorted.iloc[:24, :10].to_string(index=True).replace(' ', separator)
# print(separated_string)
# for row in homework_sorted:
#     print('{: >1} | {: >1} '.format(*row))
# print(homework[['HOUR', 'Bool']].head(24))
# homework_lost = {0: 'unknown'}
# homework['Bool'] = homework['HOUR'].apply(lambda x: '1' if x != "'unknown'" else '0')
# homework['Bool'] = homework['HOUR'].apply(lambda x: "1" if x != 'unknown' else '0')
# print(homework)
# print([homework['HOUR']!=0])