def choose_option():
    print ("Select option:")
    print ("1. ADD")
    print ("2. SUBTRACT")
    print ("3. MULTIPLY")
    print ("4. DIVISON")
    choose = input()
    while choose not in ("1","2","3","4"):
        print ("Please choose a valid option")
        print ("Select option:")
        print ("1. ADD")
        print ("2. SUBTRACT")
        print ("3. MULTIPLY")
        print ("4. DIVISON")
        choose = input()
        
    if choose == "1":
        num1 = int(input("Please enter the first number :"))
        num2 = int(input("Please eneter the second number :"))
        add_2numbers(num1,num2)
    elif choose == "2":
        
        num1 = int(input("Please enter the first number :"))
        num2 = int(input("Please eneter the second number :"))
        subtract_2numbers(num1,num2)
    elif choose == "3":
        
        num1 = int(input("Please enter the first number :"))
        num2 = int(input("Please eneter the second number :"))
        multiply_2numbers(num1,num2)
    elif choose == "4":
        
        num1 = int(input("Please enter the first number :"))
        num2 = int(input("Please eneter the second number :"))
        divide_2numbers(num1,num2)

    

def add_2numbers(n1,n2):

    print(n1+n2)

def subtract_2numbers(n1,n2):

    print(n1-n2)

def multiply_2numbers(n1,n2):

    

    print(n1*n2)

def divide_2numbers(n1,n2):

    print(n1/n2)

choose_option()
