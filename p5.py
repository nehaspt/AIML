import numpy as np
a=np.array([[1,2,4],[5,8,7]])
b=np.array([[2,1,9],[7,5,1]])
print("sum of  array is: ",a.sum())
print("max is=",a.max())
print("min is=",a.min())
print(a.min(axis=1))
print(a.max(axis=1))
print("avg of array is=",a.mean(axis=1))
print("sum of 2 array is \n",a+b)
print("mul of 2 array is \n",a*b)
print("transpose",a.T)
print("cumulative",a.cumsum())

