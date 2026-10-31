import random
playing = True
number = str(random.randint(0,9))
print("I will now generate a number from 0 to 9 and you have to guess what number it is !")
print("The whole game ends when you win")

while playing :
    guess = input("Give me your best guess ! \n")

    if number == guess :
        print("YOU WON !CONGRATULATIONS !!!!👌")
        print("The number was ...", number)
        break
    else:
        print ("Oh!No!Try again !")
    



 
    
    




