
while True:
    try:
        bill = float(input("Enter the shopping bill amount (£): "))
        if bill <= 0:
            print("Error: The bill must be greater than £0.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    try:
        discount = float(input("Enter the discount percentage (%): "))
        if discount < 0 or discount > 100:
            print("Error: Discount must be between 0 and 100.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")



discount_amount = bill * discount / 100
final_bill = bill - discount_amount
amount_of_bill = final_bill 

print("\n--- Shopping Bill Summary ---")
print(f"Original bill: £{bill}")
print(f"Discount: {discount}%")
print(f"Money saved: £{discount_amount}")
print(f"Final bill: £{final_bill}")
print(f"TOtal Bill: £{amount_of_bill}")
