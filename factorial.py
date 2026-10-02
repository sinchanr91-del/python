def factorial (x):
    '''THIS IS DOCUMENT STRING'''
    if x ==0 or x ==1:
        return 1
    else:
        return x*factorial(x -1)
print(factorial.__doc__)
print("factorial of 5 =",factorial(5))
print("factorial of 4 =",factorial(4))
print("factorial of 7 =",factorial(7))
print("factorial of 9 =",factorial(9))