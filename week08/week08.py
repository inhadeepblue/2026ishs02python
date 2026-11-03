import pandas as pd

df = pd.read_csv("APPL_price.csv")
s = df['Close'] > 175
# print(s.sum())
# print(df[s])
# print(df[s][['Open','Close']])
sc = s.cumsum()
# print(sc)
print(s.mul(sc).diff().where(lambda n: n < 0).ffill().add(sc, fill_value=0).max())
print(df[s][['Date','Close']])
