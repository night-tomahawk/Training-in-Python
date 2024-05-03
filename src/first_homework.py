# V1
import pandas as pd

pd.set_option('display.max_colwidth', 40)

crime_data = pd.read_csv('data_catalog.csv', index_col=0)
crime_data = crime_data.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)


def time_checking(line):
    target_word = 'unknown'
    if target_word in line:
        return '0'
    else:
        return '1'


crime_data['Bool'] = crime_data['HOUR'].apply(time_checking)
crime_data_sorted = crime_data.sort_values(by=['YEAR', 'MONTH'], ascending=[False, True])
print(crime_data_sorted.to_string(index=True))
