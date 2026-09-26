def greet():
    print("Welcome to the lemonade stand!")
    print("Fresh LEMONADE made just for you")
greet()
price_per_cup =float(input("Enter the price of one cup: "))
cups_sold =int(input("How many cups are sold: "))
def calculate_total(price,cup):
    total =price* cup
    return total
total_cost = calculate_total(price_per_cup,cups_sold)
rounded_total= round(total_cost,2)
print("total cost= ",rounded_total)
amount_paid =float(input("enter the amount paid by customer: "))
def calculate_change(paid,total):
    change =paid -total
    return change
change_due =calculate_change(amount_paid,rounded_total)
rounded_change =round (change_due,2)
print("=====LEMONADE STAND RECEIPT=========")
print("price per cup: ",price_per_cup)
print("cup sold: ", cups_sold)
print("total cost : ",rounded_total)
print("amount paid : ",amount_paid)
print("change due: ", change_due)
print("=========================")

