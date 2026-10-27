import seaborn as sns
import numpy as np
import pandas as pd

df = pd.read_csv('APPL_price.csv')
# print(df.info())
# print(df.head())
# print(df.tail())
# print(df['Close'])
df['Date'] = pd.to_datetime(df['Date'])  # str -> datetime
df = df.set_index('Date')  # index to datetime
# print(df.head())
# print(df['1980-12-12':'1980-12-18'])
# print(df['2022-06':'2022-06'])

# 6개월 단위 평균가
print(df.resample('6ME').mean())