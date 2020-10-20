import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

print('***Hello in "Data processing vol. 2***')

def conv_dates_series(x):  # changing strings to date format
    date_list = x.values.tolist()
    new_date_list = ['20' + i[-2:] + '-' + i[3:5] + '-' + i[0:2] for i in date_list]
    new_type_data_list = [datetime.strptime(i, "%Y-%m-%d") for i in new_date_list]
    return new_type_data_list


def set_index(df):
    df.set_index('Data/Date', inplace=True)
    return df


def drop_nan_values(x):  # mask of missing values from column
    lst_no_nan = x.dropna()
    return lst_no_nan


def clean_values(y):
    num_list = y.values.tolist()
    new_num_list = []
    for v in num_list:
        if type(v) == str:
            v = float(
                v.replace('<', '').replace('>', '').replace('\xa0', '').replace(',', '.').replace('..', '.'))
        new_num_list.append(v)
    y = new_num_list
    return y


def dict(columns):
    d = {x: columns[x] for x in range(1, len(columns))}
    print("The column indexes are as follows :  " + str(d))
    return d

con = "Y"
con_1 = "Y"
while con == "Y":

    q1 = input("Which csv file would you like to choose? Buffer_tank_data.csv or Reactor_data.csv? \n")

    def process():
        global con, con_1
        df = pd.read_csv(str(q1), header = None)
        if q1 == "Buffer_tank_data.csv":
            df.columns = [
                   'Dzień/day',
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
        if q1 == 'Reactor_data.csv':
            df.columns = [
                   'Dzień/day',
                   'Data/Date',
                   'pH',
                   'T',
                   'TCOD',
                   'SCOD',
                   'Zawiesina ogolna/TSS',
                   'Zawiesina lotna/VSS',
                   'VSS/TSS',
                   'LKT/VFA [mg/l]',
                   'LKT/VFA [meq/l]',
                   'Ca',
                   'TN',
                   'N-NH4',
                   'TP',
                   'PO4'
                ]

        df['Data/Date'] = pd.Series(conv_dates_series(df['Data/Date']))
        set_index(df)
        print(df.head())
        d = dict(df.columns)



        con_1 = "Y"
        while con_1 == "Y":
            ch_num = int(input("For which parameter would you like to get a diagram? Enter a number between 1-"
                               + str(len(df.columns) - 1) + ": \n"))
            try:
                ch_col = d[ch_num]
                print(ch_col)

                col_nam = str(ch_col)

                new_df = pd.DataFrame({col_nam: clean_values(drop_nan_values(df[col_nam])), }, columns=[col_nam])
                new_df.index = drop_nan_values(df[col_nam]).index
                print(new_df)

                plt.plot(new_df.index, new_df)
                plt.show()

            except KeyError:
                print('Incorrect value. Must be an integer from range 1-' + str(len(df.columns)-1))
                con_1 = input("Would like to enter a new value? [Y/N] \n")

            except ValueError:
                print('Incorrect value. Must be an integer from range 1-' + str(len(df.columns)-1))
                con_1 = input("Would like to enter a new value? [Y/N] \n")
            else:

                q2 = input("Would like to (enter 1, 2 or 3):\n"
                            "1. Choose next parameter in this file\n"
                            "2. Choose another file\n"
                            "3. End\n")
                if q2 == "1":
                    con_1 = "Y"
                if q2 == "2":
                    con = "Y"
                else:
                    quit()


            return df

    if q1 == "Buffer_tank_data.csv" or q1 == "Reactor_data.csv":
        process()

    else:
        print("File does not exist. Choose between Buffer_tank_data.csv or Reactor_data.csv.")
        con = input("Would like to choose another file? [Y/N] \n")
