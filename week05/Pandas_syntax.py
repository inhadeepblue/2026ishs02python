import numpy as np
import pandas as pd

df = pd.read_csv('bike.csv')
#print(df.head())
print(df.iloc[:5,0:5])
#print(df.info())
df.iloc[2, 2] = np.nan
print(df.iloc[:5,0:5])
print(df.info())
