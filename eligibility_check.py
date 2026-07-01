medical_cause =input("did you have any medical cause?press y/n")
if(medical_cause =="y"):
    print("you are allowed")
else:
    att =int(input("enter your attendance"))
    if att>= 75:
        print("you are allowed")
    else:
        print("you are not allowed")    


   