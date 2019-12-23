import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/auto.csv")
pd.options.display.float_format = '{:,.2f}'.format
print(df)

print(df.info())


print(df.horsepower.unique())
# Horsepower has unknown entries denoted by ?
# Remove those values
df = df[df.horsepower != '?'].copy()
df['horsepower'] = pd.to_numeric(df['horsepower'])

print(df.info())

# part a
print(df.head())
Quantitative  = df.select_dtypes(include=['number']).columns
Qualitative = df.select_dtypes(exclude=['number']).columns

print("Qualitative Predictors:",Qualitative)

print("Quantitative Predictors: ", Quantitative)

'''
Qualitiative Predictors: name
Quantitative Predictors: mpg, cylinders, displacement, horsepower, weight, acceleration, year, origin
'''
# part b and c
a = df.describe()
print(a)
# create range column
a.loc['range'] = a.loc['max'] - a.loc['min']
print()

print("mean, std, and range:")

#print range, mean, and std
print(a.loc[['mean','std','range']])

# part d

df2 = df.drop(index=df.index[10:85])

b = df2.describe()
b.loc['range'] = b.loc['max'] - b.loc['min']

print('New mean, std, and range:')
print(b.loc[['mean','std','range']])

# part e
g = sns.PairGrid(df,height=1.0)
g.map_upper(plt.scatter,s=3)
g.map_diag(plt.hist)
g.map_lower(plt.scatter,s=3)
plt.show()
'''
Acceleration seems normally distributed, weight and horsepower have a strong linear relationship
mpg has a strong non-linear relationship with displacement, weight, and horsepower

'''

# part f
'''
It apears that weight, displacement, and horsepower all have a strong 
non-linear negative relationship with with mpg, also year apears to have a positive relationship with mpg
All if these variables could be good predictors of mpg
'''
