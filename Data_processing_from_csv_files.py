import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
