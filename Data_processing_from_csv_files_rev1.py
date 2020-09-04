import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

T103_df = pd.read_csv('Buffer_Tank_data.csv')
print(T103_df.head())

T103_df = pd.read_csv('Buffer_Tank_data.csv', header=None)
print(T103_df.head())

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

print(T103_df['Data/Date'].values.tolist())


def conv_dates_series(x): # creating a class that changes string format to date format
    date_list = x.values.tolist()
    new_date_list = ['20' + i[-2:] + '-' + i[3:5] + '-' + i[0:2] for i in date_list]
    new_type_data_list = [datetime.strptime(i, "%Y-%m-%d") for i in new_date_list]
    return new_type_data_list

T103_df['Data/Date'] = pd.Series(conv_dates_series(T103_df['Data/Date']))
print(T103_df['Data/Date'])

T103_df.set_index('Data/Date', inplace=True)
print(T103_df.head())

print(T103_df.loc['2016-04-04'])

# Putting everything together
T103_df = pd.read_csv('Buffer_Tank_data.csv')
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

def conv_dates_series(x): # creating a class that changes string format to date format
    date_list = x.values.tolist()
    new_date_list = ['20' + i[-2:] + '-' + i[3:5] + '-' + i[0:2] for i in date_list]
    new_type_data_list = [datetime.strptime(i, "%Y-%m-%d") for i in new_date_list]
    return new_type_data_list

T103_df['Data/Date'] = pd.Series(conv_dates_series(T103_df['Data/Date']))
T103_df.set_index('Data/Date', inplace=True)
T103_df.head()


