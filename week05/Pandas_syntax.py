import numpy as np
import pandas as pd

df = pd.read_csv('bike.csv')
print(df.iloc[5:8, [0, 5, 7]])
print(df.loc[5:7, ['datetime', 'temp', 'humidity']])
#print(df.info())
print(df[df['season']==4])  # 4/4 분기 전체 행
