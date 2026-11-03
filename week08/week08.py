import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv("weight_height.csv")
# print(df[df['Weight'] > 390].index)
# print(df.iloc[2014])
df['Weight'] = df['Weight'].clip(70, 300)
print(df.iloc[2014])
# print(df.sort_values(by=['Weight']))
print(df.iloc[9285])
print(df.iloc[5360])