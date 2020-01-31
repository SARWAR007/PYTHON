list1 = [1,3,4,5]

tuple1 = tuple(list1)

print(type(tuple1))

l1= [1,3,5,6]
del l1[1]
l2= l1
print(l2)
print(l1)
print(id(l2))
print(id(l1))

l3=[]
l3 = l2.copy()
print(l3)
print(l2)
