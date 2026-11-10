import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

lifesat = pd.read_csv("lifesat.csv")
X = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

# lifesat.plot(kind='scatter', grid=True, x="GDP per capita (USD)", y="Life satisfaction")
# plt.axis([23000, 63000, 3, 10])
# plt.show()

model = LinearRegression()
model.fit(X, y)

X_new = [[33_645.77]] # South Korea's GDP per capita in 2020
print(model.predict(X_new)) # output: [[6.02986243]]
