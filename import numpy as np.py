import numpy as np
import pandas as pd

rand1=np.random.randint(1,7,size=1000)
rand2=np.random.randint(1,7,size=1000)
rand3=np.random.randint(1,7,size=1000)

rand_sum=rand1+rand2+rand3

occurrence_of_13=np.sum(rand_sum==13)

estimated_probability=(occurrence_of_13/1000)*100

print(f"Number of time the sum occured as 13 is {occurrence_of_13}")

print("Estimate how often we would see a total of 13 when throwing 3 six-sided die",estimated_probability)