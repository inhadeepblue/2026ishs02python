import pandas as pd

df = pd.read_csv('bookings.csv')
# print(df['Review'].value_counts())
# print(df.loc[df['Review'] == "Superb 9.0", "Review"])
df.loc[df['Review'] == "Superb 9.0", "Review"] = "Superb "
# print(df['Review'].value_counts())
df.loc[df['Review'] == "Superb ", "Review"] = "Superb"
df.loc[df['Review'] == "Exceptional 10", "Review"] = "Exceptional "
df.loc[df['Review'] == "Exceptional ", "Review"] = "Exceptional"
# print(df['Review'].value_counts())
# print(df['Total_Review'].unique())
df['Total_Review'] = df['Total_Review'].map(lambda x: str(x).replace('external','').strip())
df['Total_Review'] = df['Total_Review'].map(lambda x: str(x).replace('review','').strip())
df['Total_Review'] = df['Total_Review'].map(lambda x: str(x).replace(',',''))
df['Total_Review'] = df['Total_Review'].astype('float')
# print(df['Total_Review'].unique())
# print(df.info())
print(df.describe())