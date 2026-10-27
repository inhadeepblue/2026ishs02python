import seaborn as sns
import numpy as np
import pandas as pd

df = sns.load_dataset('penguins')
print(df.head())
# print(df.info())
# print(df.isna().sum())
# print(df['species'].value_counts())
print(df.groupby('species')[['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g']].mean())
df = df.groupby('species')[['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g']].apply(lambda x: x.fillna(x.mean()))
print(df.head())