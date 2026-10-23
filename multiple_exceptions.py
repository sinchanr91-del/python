try :
    num1 = int(input("enter your number"))
    num2 = int(input("enter your number"))
    result = num1 /num2
    print("Result is ", result)
except ZeroDivisionError :
    print("No zeroes !")
except ValueError :
    print("Please enter valid numbers please !")
except :
    print ("Error!Please enter a valid input please")
else :
    print("No more exceptions!")
finally :
    print("This code is perfect to execute!")
    