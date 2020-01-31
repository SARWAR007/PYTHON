add = lambda a,b:a+b

#print(add)

print(add(2,3))


var = lambda a,b: lambda c : lambda d : a+b+c+d

print(var(2,3)(4)(5))

