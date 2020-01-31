d = ('Ram-20', 'Mohan-25','rohit-30')

d2 = {}
for index in d:

    #print(index)

    #print(type(index))

    list1= index.split('-')

    d2.update({list1[0]:list1[1]})
print(d2)
print(type(d2))
print(d2.items())

for key,values in d2.items():

    print(key,':',values,end = " ")

    

    

    


    

    

    
    
