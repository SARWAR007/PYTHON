
x = int(input("Enter the original amount :"))

##y = int(input("Enter the discount % on item :"))


if x < 0:

    print("Wrong Input the amount can't be in -ve")
    x = int(input("Enter the original amount :"))

    
        
    


elif(x >= 1 and x <= 2000):

    print("Congratulations you have been allocated a discount of 10 %")

    z = x* 0.1

    final_price = x - z

    print("The final price you have to pay is : ",final_price)


elif(x >= 2001 and x <= 3000):

    print("Congratulations you have been allocated a discount of 15 %")

    z = x* 0.15

    final_price = x - z

    print("The final price you have to pay is : ",final_price)


elif(x >=3001 and x <= 5000):
    print("Congratulations you have been allocated a discount of 20 %")

    z = x* 0.2

    final_price = x - z

    print("The final price you have to pay is : ",final_price)



else:
    print("Congratulations you have been allocated a discount of 25 %")

    z = x* 0.25

    final_price = x - z

    print("The final price you have to pay is : ",final_price)
    






