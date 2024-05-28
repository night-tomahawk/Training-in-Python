# V1
import pandas as pd

crime_data = pd.read_csv('crime_catalog.csv', index_col=0)


def time_checking(line):
    target_word = 'unknown'
    if target_word in line:
        return '0'
    else:
        return '1'


crime_data['Bool'] = crime_data['HOUR'].apply(time_checking)
crime_data_sorted = crime_data.sort_values(by=['YEAR', 'MONTH'], ascending=[False, True])
print(crime_data_sorted.to_string(index=True))
