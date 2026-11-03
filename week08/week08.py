import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv("weight_height.csv")
print(df.describe())
print(df.info())
sns.scatterplot(x='Weight', y='Height', data=df)
plt.show()

print(df.sort_values(by='Weight', ascending=False))
