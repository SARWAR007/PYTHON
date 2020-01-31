count = 0 
while True: 
    userName = input("Hello! Please provide your Username: ") 
    password = input("Password: ")
    count += 1
    print(count)
    if count == 3: 
        print("Login chances exhausted .You have entered wrong credentials", count,"times.")
        break 
    else:
        if userName == 'farhan' and password == 'password':
            print("Login successfull!!!!")
            break 
        else:
            continue
            
   

        
