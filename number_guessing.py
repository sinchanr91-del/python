import random 
secret_number = random.randint(1,50)
i =1
for  i in range(1,7):

    guess = int(input("enter your number"))
    if guess ==secret_number:
        print("Wow!you have got it correct")
    else:
        print("You now have  1 less hearts,")
print(" the secret number was...",secret_number)


