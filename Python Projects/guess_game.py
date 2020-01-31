import random


magicNumber = random.randrange(1,20)

while True:
    print('Take a guess !')
    guess = int(input())

    if guess < magicNumber :
        print('Your Number is wrong and small')
    elif guess > magicNumber:
          print('Your Number is wrong and  high')
    elif guess == magicNumber:
        
        
        print('You guessed the number correctly ')
        break

    
        
    
