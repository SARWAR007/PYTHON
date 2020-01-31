list1 = [10,20,30,40]
#list1.extend([50,60,70])
list1.count(10)

print(list1.count(10))

x = list1.index(40,1,len(list1))
print("List index",x)

print(list1)


tuple1 =(10,20,30,40)



#print(tuple1)

print(max(list1))
print(max(tuple1))

list1.pop(2)
print(list1)
list1.remove(10)
print(list1)
list1[1]=50

print(list1)


list1 = [2,3,4]

list2 = list1.copy()

print(id(list1))
print(id(list2))

print(list2 is list1)


list5 = [1,3,5,6,7,7]
print(set(list5))

list5.clear()
print(list5)
