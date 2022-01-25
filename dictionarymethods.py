dic = {1:'apple', 2:'grapes', 3:'mango'}
print('original: ', dic)

# Accessing value for key
print(dic.get(1))

# Accessing keys for the dictionary
print(dic.keys())

# Accessing keys for the dictionary
print(dic.values())

# Printing all the items of the Dictionary
print(dic.items())
# copy method
dic1=dic.copy()
print('the new copied dictionary: ',dic1)
#pop
dic.pop(2)
print(dic)
#popitem
dic.popitem()
print(dic)
#setdefault
value=dic1.setdefault(2)
print(value)
value1=dic1.setdefault(4,'banana')
print(dic1)

# of update() method in Dictionary

# Dictionary with three items
Dictionary1 = {'A': 'apple', 'B': 'ball', }
Dictionary2 = {'B': 'banana'}

# Dictionary before Updation
print("Original Dictionary:")
print(Dictionary1)

# update the value of key 'B'
Dictionary1.update(Dictionary2)
print("Dictionary after updation:")
print(Dictionary1)
#clear
Dictionary1.clear()
print(Dictionary1)
#fromkeys()

# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }

vowels = dict.fromkeys(keys)
print(vowels)


