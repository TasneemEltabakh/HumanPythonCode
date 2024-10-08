import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
age = pd.cut(df['age'], [0, 20, 55])
result = df.pivot_table('survived', index=['sex', age], columns='class')
print(result)
