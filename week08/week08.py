import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress
import pandas as pd

df = pd.read_csv('Uber.csv')
df['START_DATE*'] = pd.to_datetime(df['START_DATE*'], errors='coerce')
df['END_DATE*'] = pd.to_datetime(df['END_DATE*'], errors='coerce')
df = df.sort_values(['START_DATE*','END_DATE*'])
df = df.drop(1155)
df['DURATION*'] = (df['END_DATE*'] - df['START_DATE*']).dt.total_seconds() / 60
df = df.dropna()

slope, intercept, relation, _, _ = linregress(df['MILES*'], df['DURATION*'])

fig, ax = plt.subplots()
sns.regplot(x='MILES*', y='DURATION*', data=df, ax=ax, line_kws={'label':f'y={slope:.2f}x+{intercept:.2f}, R^2={relation**2:.2f}'})
plt.legend()
plt.show()