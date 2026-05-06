# Rule of 72, years to double money

savings = 77064.49
interest_rate = 4.20
savings_double = savings * 2
years_to_double = 72 / interest_rate

print(f"Your current savings is ${savings:,.2f}. At a {interest_rate:.2f}% interest rate, your savings account will be worth ${savings_double:,.2f} in {years_to_double:.1f} years.")