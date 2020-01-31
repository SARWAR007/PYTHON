list1 = list(input("Enter the 5 elements you want to enter in list").split(" "))
list2 = []
while True:
    maximum = list1[0]  
    for x in list1: 
        if x > maximum:
            
            maximum = x
            
    list2.append(maximum)
    list1.remove(maximum)
    
    if(len(list1) == 0):
        break
    
print(list2)
