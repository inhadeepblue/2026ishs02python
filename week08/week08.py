import numpy as np
import pandas as pd

s = pd.Series([0, 0, 1, 1, 0, 1, 1, 1, 1, 0])
sc = s.cumsum()
# print(sc)
# print(s.mul(sc))
# print(s.mul(sc).diff())
# print(s.mul(sc).diff().where(lambda n: n < 0))
# print(s.mul(sc).diff().where(lambda n: n < 0).ffill())  # forward (bfill : backward fill)
# print(s.mul(sc).diff().where(lambda n: n < 0).ffill().add(sc, fill_value=0))
print(s.mul(sc).diff().where(lambda n: n < 0).ffill().add(sc, fill_value=0).max())