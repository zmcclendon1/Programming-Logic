employee_name = input("Employee’s name: ")
num_shifts = int(input("Number of Shifts: "))
num_transactions = int(input("Number of transactions: "))
transaction_value = float(input("Transaction dollar value: "))

productivity_score = (transaction_value / num_transactions) / num_shifts

if productivity_score <= 30:
    bonus = 50.00
else:
    if productivity_score <= 69:
        bonus = 75.00
    else:
        if productivity_score <= 199:
            bonus = 100.00
        else:
            bonus = 200.00

print("Employee Name:", employee_name)
print("Employee Bonus: $" + str(bonus))