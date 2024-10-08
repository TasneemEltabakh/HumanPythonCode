import pandas as pd 
import numpy as np
sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'],
          ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
sales_tuples = list(zip(*sales_arrays))
sales_index = pd.MultiIndex.from_tuples(sales_tuples, names=['sale', 'city'])
print(sales_tuples)
print("\nConstruct a Dataframe using the said MultiIndex levels: ")
df = pd.DataFrame(np.random.randn(8, 5), index=sales_index)
print(df)

print("\nExtract a single row from the said dataframe:")
print(df.loc[('sale2', 'city2')])
print("\nExtract a single row from the said dataframe:")
print(df.loc[('sale2', 'city2')])

print("\nExtract number of rows from the said dataframe:")
print(df.loc['sale1'])
print("\nExtract number of rows from the said dataframe:")
print(df.loc['sale3'])

print("\nExtract a single value from the said dataframe:")
print(df.loc[('sale1', 'city2'), 1])
print("\nExtract a single value from the said dataframe:")
print(df.loc[('sale4', 'city1'), 4])
