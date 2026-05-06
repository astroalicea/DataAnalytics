#Calculation of net worth

# Assests
real_estate = 3709030
cars = 520519
boat = 755870
cash = 499991
investments = 3490831
business_equity = 985360
valuables = 2550600

#Debt 
credit_card = 594501
mortages = 700000


total_assets = real_estate + cars + boat + cash + investments + business_equity + valuables
print(f"Total assets are:  ${total_assets:,.2f}")

total_debt = credit_card + mortages
print(f"Total debt are:  ${total_debt:,.2f}")

net_worth = total_assets - total_debt
print(f"Total net worth is:  ${net_worth:,.2f}")