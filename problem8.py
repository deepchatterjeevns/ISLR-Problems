
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
pd.options.display.float_format = '{:,.2f}'.format
college = pd.read_csv("data/College.csv")
#print(college)
college = college.set_index("Unnamed: 0")
college.index.name = 'Names'
print(college.head())
print(college.describe(include="all"))
g = sns.PairGrid(college,vars  =college.iloc[:,1:11],hue='Private')
g.map_upper(plt.scatter,s=3)
g.map_diag(plt.hist)
g.map_lower(plt.scatter,s=3)
g.fig.set_size_inches(12, 12)
plt.show()
sns.boxplot(x='Private', y='Outstate', data=college)
plt.show()
college.loc[college['Top10perc']>50, 'Elite'] = 'Yes'
college['Elite'] = college['Elite'].fillna('No')
sns.boxplot(x='Elite', y='Outstate', data=college)
plt.show()
