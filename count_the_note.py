amount = int(input("enter the amount: "))
note1 = amount//100
note2 = (amount%100)//50
note3 = ((amount%100)%50)//10
print("number of hundred rupees notes =",note1)
print("number of fifty rupees notes =",note2)
print("number of ten rupees notes =",note3)
