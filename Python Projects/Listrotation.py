list = [10,20,30,40]

n = int(input("Enter the step size :"))

while(n > 0):
    temp = list[-1] ##store the first element first in temporary value
    for index in range(len(list)-1):
        list[index+1] = list[index]
        print(list[index+1])
    ##list[index] = temp
    n = n -1
    
print(list)
