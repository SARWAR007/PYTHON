


d = {"name" : "Rohit","age":"25","Roll":'21'}

print(d["name"])
print(d.get("name"))

#print(d.get("course"))

d["name"] = "Farhan"
d.update({'name':'xyz'})
print(d)
d["course"] = "Python"
print(d)
d.update({'Course':'C++'})
print(d)
x = d.pop("age")
print(x)
y = d.items()
print(type(y))
for index,values in d.items():
    print(index ,':',values ,end = ",")
    print(type(index))
    

d4 = {'1':1,'2' :2 ,'3':3}
d5 = d4.copy()
print(d5)
d5.fromkeys([0,1,2],"xyz")
print(d5)


d6 = {"a":1,"b":2}

d6.setdefault("d",'a')
print(d6)


