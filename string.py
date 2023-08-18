fruits = ["mango","apple","orange","kiwi"]
x = list(filter(lambda x:'g' in x ,fruits))
print(x)
print()
y= list(filter(lambda x:'g' not in x,fruits))
print(y)

#animals
print()
animals = ["cat","goat","sheep","snail","dog"]
x = list(filter(lambda x:'at' in x ,animals))
print(x)
print()
y= list(filter(lambda x:'at' not in x,animals))
print(y)
