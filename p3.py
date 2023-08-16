import pandas as pd

data = pd.read_csv("C:/Users/SPTINT-03/Desktop/dataset1/iris.csv")
print(data)
print(data.head(5))
print(data.tail(10))
print(data['SepalWidthCm'])
print(data.count())
print(data.info())
print(data.dtypes)

