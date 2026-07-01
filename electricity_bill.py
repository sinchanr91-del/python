unit =int(input("please enter the units you have consumed"))
if unit < 50:
    amount= unit*2.60
    tax =25
elif unit <= 100:
    amount= unit*3.25
    tax =35
elif unit <= 200:
    amount= unit*5.26
    tax =45
else:
    amount= unit*8.45
    tax =75
total =amount +tax
print("electricity bill= ",total)


    
    

