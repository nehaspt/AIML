import numpy as np

a = np.array([[1,2,3],[5,8,7]],dtype='float')
print("\n Array created using padded list \n",a)

b = np.array((1,3,4))
print("\n Array created using passed type:\n",b)

c=np.zeros((3,4))
print("\n Array intialized with all zeros:\n",c)

d=np.full((3,3), 6,dtype='complex')
print("\n Array intialized with all 65","Array type is complex:\n",d)

e = np.random.random((2,2))
print("\n A random array:\n",e)

f = np.arange(0,30,5)
print("\n A sequencial array with steps of 5:\n",f)

g = np.linspace(0,5,10)
print("\nA sequencial array with 10 values between","0 and 5:\n",g)

arr = np.array([[1,2,3,4],[5,2,4,2],[1,2,0,1]])

newarr = arr.reshape(2,2,3)
print("\n original array:\n",arr)
print("Reshaped array:\n",newarr)

arr = np.array([[1,2,3],[4,5,6]])
flarr = arr.flatten()

print("\n Original array:\n",arr)
print("Flattened array:\n",flarr)


