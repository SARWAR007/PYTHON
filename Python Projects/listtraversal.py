address = ["Global Meadows Apartment","JHBCS Layout"]
pins = {"PHONE" : 220594 ,"ATM" : 8865 , "Passwd" : 1234}

print(address[0],address[1])


pin = int(input("Enter values for pin : "))

def find_in_file_loc(f):
    myfile = open("fruits.txt")
    fruit = myfile.read()
    fruit = fruit.splitlines()
    
    

    if  f in fruit:
           return "We got the fruit"

    else:
        return "We didn't find the fruit"



if pin in pins.values():
    fruit = input("Enter the name of fruits : ")
    print(find_in_file_loc(fruit))

else:
    print("Incorrect Pin!!")
    print("This info contains the pins of following account")
    for key in pins.keys():
        print(key)



