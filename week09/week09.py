import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

lifesat = pd.read_csv("lifesat.csv")
print(len(lifesat))
print(lifesat.info())
X = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values
# df_X = pd.DataFrame(X, columns=["GDP per capita (USD)"])
# print(df_X.tail())

