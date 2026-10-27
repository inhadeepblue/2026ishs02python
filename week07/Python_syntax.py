import seaborn as sns
import pandas as pd

df = sns.load_dataset('titanic')
# print(df.head())
# print(df.tail())
# print(df.describe())
print(df.info())
print(df['survived'].value_counts())
print(df['alive'].value_counts())
print(df['embark_town'].value_counts())
print(df['embarked'].value_counts())
print(df['pclass'].value_counts())
print(df['class'].value_counts())