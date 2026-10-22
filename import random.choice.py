import random

outcomes=[2,3,4,5,6,7,8,9,10,11,12]
weights=[1,2,3,4,5,6,5,4,3,2,1]
k=10

result=random.choices(outcomes,weights=weights,k=k)
print("stimutlated rolls:",result)