from functools import reduce

print("map function")
lst= [1,2,3,4,5]
l = list(map(lambda a: a+5 , lst))
print(l)
print()

print("filter function")
lst=[1,2,3,4,5,6,7,8]
l = list(filter(lambda x:x%2==0,lst))
print(l)
print()

print("reduce function")
lst = [1,2,3,4,5,6,7,8,9]
y = reduce(lambda x,y:x+y,lst)
print(y)
print()

print("largest of a numbers")
lst1 = [1,2,3,4,5,6]
x = reduce(lambda a,b: a if(a>b) else b,lst1)
print(x)
