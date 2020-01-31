def add(a,b):

    var = lambda c: a+b+c
    print(var(4))

    return  lambda c: a+b+c

add(2,3)

