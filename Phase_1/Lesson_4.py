#The Smart ATM Withdrawal Simulator

balance = 500.00
print(f"Your current balance is: R{balance:.2f}")
withdrawal_amount = float(input("Enter the amount you want to withdraw: "))
if withdrawal_amount <= balance:
    balance -= withdrawal_amount
    print(f"Withdrawal successful! Your new balance is: R{balance:.2f}")
else:
    print("Insufficient funds for this withdrawal.")
