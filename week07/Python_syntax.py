import seaborn as sns
import numpy as np
import pandas as pd

def get_IQR(data):
    _3rd = data.quantile(.75)
    _1st = data.quantile(.25)
    return (np.abs(_3rd - _1st) * 1.5)

df = sns.load_dataset('titanic')
# print(df.info())
df1 = df.drop(['alive', 'class', 'embarked'], axis=1)
# print(df1.info())
# print(df1.groupby('sex')['survived'].mean())
# print(df1.groupby(['sex','pclass'])['survived'].mean())
# print(df1.groupby(['sex','pclass'])['survived'].agg(['mean','median','count']))
# print(df1.groupby(['sex','pclass'])[['survived','age']].agg({'survived':'mean','age':'median'}))
print(df1.groupby(['sex','pclass'])['age'].apply(get_IQR))