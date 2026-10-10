def calculate_change(paid,price) :
    change =paid - price

    return change
snack_price =25
print ("===============SNACK VENDING MACHINE===============")
print("The snacks cost : ", snack_price)
print ("Accepted coins :  1,5,10,25")
total_inserted = 0
coins_inserted =0

while True :
    coin = int(input("insert a coin: 1,5,10,25 "))
    if coin != 1 and coin != 5 and coin !=10 and coin != 25 :
        print(" INVALID COIN ! TRY AGAIN !")
        continue 
    total_inserted = total_inserted + coin
    coins_inserted = coins_inserted +1
    print (" TOTAL INSERTED  : ", coin)
    print(" Total so far : ", total_inserted)
    if total_inserted >= snack_price :
        print ("Enough money inserted")
        break
change_due = calculate_change(total_inserted,snack_price)
print(" Dispensing your snacks....")
if change_due == 0 :
    pass
else :
    print("Here is your change!", change_due)

print("^^^^^^^^PURCHASE SUMMARY^^^^^^^^^")
print("Snack price : ", snack_price)
print("Coins Inserted : ", coins_inserted)
print("Total Paid :",total_inserted)
print("Change Give :", change_due)
print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("THANKS FOR YOUR PURCHASE")