l1=[10,12,13]
print(l1[-1])
print(l1[-2])
# Python3 code to demonstrate working of
# Negative index of Element
# Using index() + len()

l2 = [5, 7, 8, 2, 3, 5, 1]

print("The original list is : " + str(l2))

# initializing Element
K = 3

# getting length using len() and subtracting index from it
res = len(l2) - l2.index(K)

# printing result
print("The required Negative index : -" + str(res))

