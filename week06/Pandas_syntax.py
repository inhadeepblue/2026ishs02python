import numpy as np
import pandas as pd
df = pd.read_csv('bike.csv')

df.rename({'registered':'registered_user','casual':'casual_user','temp':'temperature', 'atemp':'apparent_temperature'}, axis=1, inplace=True)
print(df.info())
