import numpy as np
import pandas as pd

random1_100=np.random.randint(1,7,size=100)

random2_100=np.random.randint(1,7,size=100)

sum_100=random1_100+random2_100
print(sum_100)

series_100=pd.Series(sum_100).value_counts().sort_index()
print(series_100)

print("="*100)

random1_1000=np.random.randint(1,7,size=1000)

random2_1000=np.random.randint(1,7,size=1000)

sum_1000=random1_1000+random2_1000
print(sum_1000)

series_1000=pd.Series(sum_1000).value_counts().sort_index()
print(series_1000)

print("="*100)

random1_1000000=np.random.randint(1,7,size=1000000)

random2_1000000=np.random.randint(1,7,size=1000000)

sum_1000000=random1_1000000+random2_1000000
print(sum_1000000)

series_1000000=pd.Series(sum_1000000).value_counts().sort_index()
print(series_1000000)