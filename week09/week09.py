import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor

lifesat = pd.read_csv("lifesat.csv")
X = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

print(lifesat)

# lifesat.plot(kind='scatter', grid=True, x="GDP per capita (USD)", y="Life satisfaction")
# plt.axis([23000, 63000, 3, 10])
# plt.show()

# model = LinearRegression()
model = KNeighborsRegressor(n_neighbors=3)
model.fit(X, y)

X_new = [[33645.77]] # South Korea's GDP per capita in 2020
print(model.predict(X_new)) # 선형회귀모델: [[6.02986243]], 최근접이웃모델:[[5.73333333]]
