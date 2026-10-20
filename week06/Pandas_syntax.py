import pandas as pd

df = pd.read_csv('bookings.csv')
df.loc[df['Review'] == "Superb 9.0", "Review"] = "Superb "
df.loc[df['Review'] == "Superb ", "Review"] = "Superb"
df.loc[df['Review'] == "Exceptional 10", "Review"] = "Exceptional "
df.loc[df['Review'] == "Exceptional ", "Review"] = "Exceptional"
df['Total_Review'] = df['Total_Review'].map(lambda x: str(x).replace('external','').strip())
df['Total_Review'] = df['Total_Review'].map(lambda x: str(x).replace('review','').strip())
df['Total_Review'] = df['Total_Review'].map(lambda x: str(x).replace(',',''))
df['Total_Review'] = df['Total_Review'].astype('float')
# print(df[df['Rating'].isna()].tail().index)
# print(df.describe())
# print(df['Rating'].head())
# print(df['Rating'].tail())
index = df[df['Rating'].isna()].tail().index
df['Rating'] = df['Rating'].fillna(df['Rating'].median())
print(df.loc[index, ['Rating', 'Total_Review']])