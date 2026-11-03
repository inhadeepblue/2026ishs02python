import pandas as pd

df = pd.read_csv('German_credit.csv')
ages = [10, 20, 30, 40, 50, 60, 70, 80]
# print(pd.cut(df['Age'], bins=ages, right=False).reset_index().groupby('Age').size())
print(pd.qcut(df['Age'], q=8, duplicates='drop').reset_index().groupby('Age').size())
