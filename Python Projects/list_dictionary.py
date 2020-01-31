str = "I am the Coder."

list1 = list(str)
print(list1)
list2=[]
dict_1 = {'I':'@A','a':'@M','m':'4#','T':'@2'}
str1=""


for index in range(len(list1)):

    
    if list1[index] in dict_1.keys():
        list2.append(dict_1.get(list1[index]))
    else:
        list2.append(list1[index])
print(list2)


for x in list2:
    

    str1 += x

print(str1)
        

        
