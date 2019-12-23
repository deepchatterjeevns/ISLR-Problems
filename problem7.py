import numpy as np
import pandas as pd
data = {'X1' : pd.Series([0,2,0,0,-1,1]),
     'X2' : pd.Series([3,0,1,1,0,1]),
     'X3' : pd.Series([0,0,3,2,1,1]),
     'Y' : pd.Series(['Red','Red','Red','Green','Green','Red'])
}
df = pd.DataFrame(data)
df.index = np.arange(1, len(df) + 1)
print(df)
# part a
df['distance'] = np.sqrt(df['X1']**2+df['X2']**2+df['X3']**2)

print(df.sort_values(by = 'distance'))
# part b k = 1
# after sorting by distance from the origin, we can see that the nearest neighbor is green. So our prediction for k = 1
# would be green
# part c k = 3
# for k = 3 our prediction would be red because 2/3 of the nearest neighbors are red
# part d
# for non-linear decision boundary, the best value of k would be small in order to capture local non-linearity
# for large k the bayes decision boundary becomes more linear

