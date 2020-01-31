d = {'Ram' : 30 , 'Shyam': 20 ,'Rohit': 30 ,'Sam':20}
d2= d.copy()
for key,value in d2.items():

    if(key == 'Shyam'):

        d[key] = '50'

    if(value == 30):

        d["Farhan"] = d.pop(key)

    
    

    

        
        
print(d)



        

    


    
