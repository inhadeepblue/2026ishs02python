import numpy as np
import pandas as pd

s = pd.Series([1, np.nan, np.nan,2, np.nan, 3])
print(s)
s = s.bfill()  # backward fill (ffill : forward fill)
print(s)