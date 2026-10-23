valid = False 
while not valid:
    try:
        n = int(input("enter your number"))
        while n % 2 == 0:
            print("Bye!Have a good day!")
            n = int(input("Enter your number please"))
        valid = True
    except ValueError:
        print("Invalid!")
    
        
