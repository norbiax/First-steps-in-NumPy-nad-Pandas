import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()
print('*** Welcome in "Data processing vol. 1 "***')


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


def set_df(file_name):
    df = pd.read_csv(str(file_name), header=None)
    if file_name == "Buffer_tank_data.csv":
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
    if file_name == 'Reactor_data.csv':
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
    return df


con = "Y"
con_1 = "Y"
con_2 = "Y"


def make_graph():
    global con_1
    con_1 = "Y"
    while con_1 == "Y":
        df = set_df(q1)
        d = dict(df.columns)
        try:
            ch_num = int(input("For which parameter would you like to get a graph? Enter a number between 1-"
                               + str(len(df.columns) - 1) + ": \n"))
            ch_col = d[ch_num]
            print(ch_col)
            col_nam = str(ch_col)
            new_df = pd.DataFrame({col_nam: clean_values(drop_nan_values(df[col_nam])), }, columns=[col_nam])
            new_df.index = drop_nan_values(df[col_nam]).index
            print(new_df)
            plt.plot(new_df.index, new_df)
            plt.show()
            con_1 = input("Choose next parameter in this file [Y/N]\n")
        except KeyError:
            con_1 = input('Incorrect value. Must be an integer from range 1-' + str(len(df.columns) - 1)
                          + "\nWould like to enter a new value? [Y/N] \n")
            if con_1 != "Y":
                break
        except ValueError:
            con_1 = input('Incorrect value. Must be an integer from range 1-' + str(len(df.columns) - 1)
                          + "\nWould like to enter a new value? [Y/N] \n")
            if con_1 != "Y":
                break


def num_of_nulls():
    df = set_df(q1)
    print(df.isnull().sum())


def fun1():
    global con_2
    while con_2 == "Y":
        op_sel = str(input('What would you like to do? Enter a number from 1 to 2.\n'
                           '1. Generate a graph with the values of the selected parameter for the entire '
                           'period\n'
                           '2. Check how many values are missing in each column\n'))
        if op_sel == "1":
            make_graph()
            q2 = (input("Next task in current file (" + q1 + ") - 1\n"
                        "Choose another file - 2\n"
                        "Exit - 3\n"))
            if q2 == "1":
                continue
            if q2 == "2":
                break
            else:
                print("Good bye!")
                quit()
        if op_sel == '2':
            num_of_nulls()
            q2 = (input("Next task in current file (" + q1 + ") - 1\n"
                        "Choose another file - 2\n"
                        "Exit - 3\n"))
            if q2 == "1":
                continue
            if q2 == "2":
                break
            else:
                print("Good bye!")
                quit()
        else:
            q3 = input("Incorrect value. Must be an integer from range 1-2. \n"
                       "Would like to (type 1 or 2):\n"
                       "1. Try again\n"
                       "2. Choose another file\n")
            if q3 == "1":
                continue
            else:
                break


while con == "Y":
    q = str(input("Which csv file would you like to choose?\n"
                  "Buffer_tank_data.csv - 1\n"
                  "Reactor_data.csv - 2 \n"))
    if q == "1":
        q1 = "Buffer_tank_data.csv"
        fun1()
        continue
    if q == "2":
        q1 = "Reactor_data.csv"
        fun1()
        continue
    else:
        con = input("Wrong file name or file does not exist. Choose between "
                    "Buffer_tank_data.csv or Reactor_data.csv.\n"
                    "Would like to choose again? If 'yes' type 'Y'. Otherwise, you will exit the program\n")
        if con != "Y":
            print("Good bye!")
            quit()
