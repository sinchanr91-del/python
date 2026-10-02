def total_calculate (bill_amount, per):
    tip_amount = (per/100)*bill_amount
    total = bill_amount +tip_amount
    print ("Total amount to pay: ",total)
total_calculate(1000,10)
    
    