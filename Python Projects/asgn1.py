list = ['a','b','c','d','e']

n = len(list)
while_i=0


while(while_i < n):
    for row in range(0,n):
        for col in range(0,row+1):
            print(list[col],end =" ")
            
        print()
     
            
    while_i+=1
    print('-------------------------')
