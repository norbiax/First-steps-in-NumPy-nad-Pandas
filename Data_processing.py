import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print(pd.__version__)

# Data input
raw_wastewater_data = [
    ['25-01-16', 530, 349, 295, 56,	5.80, None, 6400, 2315, None, 1.9, None, 1053, 18, 13, None, 1.4, 4, 0.2, 6.4],
    ['26-01-16', 291, 270,	200, 77, 4.77, None, 10000, 4369, None, 2.0, None, 1418, 24, 96, 94.3, 1.2, 11,	0.5, 10.7],
    ['27-01-16', 59, 167, 200, 80,	4.55, None,	10800, 4843, None, 1.4,	None, 1950, 32, 102, None, 0.8,	5,	0.3, 13],
    ['28-01-16', 266, 190, 225,	67,	4.37, 22.6,	9400, 3913, None, 2.2,	None, 1907,	32,	77,	69,	1.1, 4,	None, 17.2],
    ['29-01-16', -77, None, None, 76, 4.52, 22.8, 10700, 4026, None,	2.0, None, 1642, 27, 104, None, 1.0, 17, None, 15.4]
]

# Create a data_df pandas DataFrame with the given raw wastewater data
data_df = pd.DataFrame(data=raw_wastewater_data)

# Add columns names
col_names = [
    'date',
    'Flow_FC101_raw_sewage',
    'Flow_FC101_outlet_from_T102',
    'Flow_FC102_inlet_to_BB',
    'Level',
    'pH',
    'T',
    'TCOD',
    'SCOD',
    'BOD5',
    'TSS',
    'VSS',
    'VFA mg/l',
    'VFA meq/l',
    'TN',
    'TKN',
    'NH4',
    'NO3',
    'NO2',
    'TP'
]

data_df.columns = col_names

# Add index names to the data_df (using the dates as index)
data_df.index = data_df['date']
data_df = data_df.drop('date', axis=1)

# Show the first 5 elements on data_df
print(data_df.head())

# Show the last 5 elements on data_df
print(data_df.tail())

# Show the TP values of all middle elements on data_df
print(data_df.iloc[1:-1].TP.to_frame())

# Show the first and last TP values on data_df
print(data_df.iloc[[0, -1],][['TP']])

#print(data_df)