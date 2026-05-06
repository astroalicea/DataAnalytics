# Rule of 72, years to double money

savings = float(input("What is your current savings? "))

interest_rate = float(input("What is your interest rate? "))

savings_double = savings * 2

years_to_double = 72 / interest_rate

print(f"Your current savings is ${savings:,.2f}. At a {interest_rate:.2f}% interest rate, your savings account will be worth ${savings_double:,.2f} in {years_to_double:.1f} years.")

# Possible pitfalls with input()
# 1. If user inputs letters or words instead of numbers,
#    the script will give ValueError.
# 2. If user user enters 0 for the interest rate, the script will crash
#    with a ZeroDivisionError since you cant devide my zero.
