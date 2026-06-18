print("enter marks obtained in five subject")
m1 =int(input())
m2 =int(input())
m3 =int(input())
m4 =int(input())
m5 =int(input())
total = m1+m2+m3+m4+m5
avg= int(total/5)
validrange= range(0,101)

if avg not in validrange:
    print("invalid input")

elif avg in range(91,101):
    print("your grade is A1")#

elif avg in range(81,91):
    print("your grade is A2")

elif avg in range(71,81):
    print("your grade is B1")

elif avg in range(61,71):
    print("your grade is B2")

elif avg in range(51,61):
    print("your grade is C1")

elif avg in range(41,51):
    print("your grade is C2")

elif avg in range(31,41):
    print("your grade is D1")

elif avg in range(21,31):
    print("your grade is D2")

elif avg in range(1,21):
    print("your grade is E")
