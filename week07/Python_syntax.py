import seaborn as sns
import pandas as pd

df = sns.load_dataset('titanic')
# print(df.info())
df1 = df.drop(['alive', 'class', 'embarked'], axis=1)
# print(df1.info())
# print(df1.groupby('sex')['survived'].mean())
# print(df1.groupby(['sex','pclass'])['survived'].mean())
# print(df1.groupby(['sex','pclass'])['survived'].agg(['mean','median','count']))
print(df1.groupby(['sex','pclass'])[['survived','age']].agg({'survived':'mean','age':'median'}))