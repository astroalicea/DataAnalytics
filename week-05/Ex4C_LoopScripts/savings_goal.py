# savings goal

bank_balance = 5000
savings_goal = 50000
weekly_savings = 1000
treat = 100

while bank_balance < savings_goal:
    bank_balance += weekly_savings

    if bank_balance >= savings_goal * .75:
        bank_balance -= treat
        print(f"So close! After treating myself, my balance is up to {bank_balance:,.2f}")
    elif bank_balance >= savings_goal * .5:
        print(f"Almost there! This week my balance is up to {bank_balance:,.2f}")
    else:
        print(f"This week my balance increased to ${bank_balance:,.2f}")

print(f"Goal met! My current balance is {bank_balance:,.2f}.")
