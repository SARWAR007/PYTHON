

list1 = list(input("Enter the 5 elements you want to enter in list").split(" "))
list2 = []
while True:
    minimum = list1[0]  
    for x in list1: 
        if x < minimum:
            
            minimum = x
            
    list2.append(minimum)
    list1.remove(minimum)
    
    if(len(list1) == 0):
        break
    
print(list2)
