import pandas as pd

homework = pd.read_csv('D:/programing/python-base/homework.csv', index_col=0)


def check_hour_passenger(word):
    if len(word) < 5:
        return '1'
    else:
        return '0'


homework['Bool'] = homework['HOUR'].apply(check_hour_passenger)
homework_sorted = homework.sort_values(by=['YEAR', 'MONTH'], ascending=[False, True])
pd.set_option('display.max_colwidth', 40)
print(homework_sorted.to_string(index=True))
