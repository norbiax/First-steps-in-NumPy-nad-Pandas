import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

T103_df = pd.read_csv('Buffer_Tank_data.csv')

T103_df = pd.read_csv('Buffer_Tank_data.csv', header=None)

T103_df.columns = ['Dzień/day',
                   'Data/Date',
                   'Przepływ/Flow - z zakladu',
                   'Przepływ/Flow F1',
                   'Przepływ/Flow F2',
                   'Poziom Level',
                   'pH',
                   'T',
                   'Ladunek ChZT T103/Ladunek proj.',
                   'Ładunek ChZT całk. w zbiorniku buforowym',
                   'Ladunek zawiesiny w T103',
                   'ChZT calk. W zbiorniku buforowym/TCOD',
                   'ChZT filtr. W zbiorniku buforowym',
                   'Sredni poziom w buforze',
                   'HRT',
                   'Zawiesina ogolna/TSS',
                   'Ladunek azotu ogolnego w T103',
                   'Ladunek fosforu ogolnego w T103',
                   'ChZT calk./TCOD',
                   'ChZT filtr./SCOD',
                   'Zawiesina ogolna/TSS',
                   'LKT/VFA',
                   'Pre-acidicification',
                   'LKT/VFA',
                   'TN',
                   'TKN',
                   'N-NH4',
                   'NO3',
                   'NO2',
                   'TP',
                   'PO4',
                   'Cl'
]
print(T103_df.shape)
print(T103_df.head())
print(T103_df.tail(3))
print(T103_df.dtypes)

def conv_dates_series(x): # changing strings to date format
    date_list = x.values.tolist()
    new_date_list = ['20' + i[-2:] + '-' + i[3:5] + '-' + i[0:2] for i in date_list]
    new_type_data_list = [datetime.strptime(i, "%Y-%m-%d") for i in new_date_list]
    return new_type_data_list

T103_df['Data/Date'] = pd.Series(conv_dates_series(T103_df['Data/Date']))

T103_df.set_index('Data/Date', inplace=True)

print(T103_df.info())

def drop_nan_values(x): # mask of missing values from column
    lst_no_nan = x.dropna()
    print(lst_no_nan)
    return lst_no_nan

def clean_values(y): # removing undesirable signs from the values to obtain specific numbers
    num_list = y.values.tolist()
    new_num_list = []
    for v in num_list:
        if type(v) == str:
            v = float(v.replace('<', '').replace('>', '').replace('\xa0', '').replace(',', '.').replace('..','.'))
        new_num_list.append(v)
    y = new_num_list
    return y

d = {x : T103_df.columns[x] for x in range(1, len(T103_df.columns))}
print("The column indexes are as follows :  " + str(d))
ch_num = int(input("For which parameter would you like to get a diagram? Enter a number between 1-30: \n"))
ch_col = d[ch_num]
print(ch_col)

col_nam = str(ch_col)

df = pd.DataFrame({col_nam: clean_values(drop_nan_values(T103_df[col_nam])),}, columns=[col_nam])
df.index = drop_nan_values(T103_df[col_nam]).index
print(df)

plt.plot(df.index, df)
plt.show()

