#Function 1 - Mailing label
def display_mailing_label(name, address, city, state, zip):
    print(f"{name}")
    print(f"{address}")
    print(f"{city}, {state} {zip}")

#Function 2 - Add any number of integers
def add_numbers(*args):
    result = sum(args)
    equation = ' + '.join(str(n) for n in args)
    print(f"{equation} = {result}")

# Function 3 - Receipt
def display_receipt(total_due, amount_paid):
    print(f"Total Due: ${total_due:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}")
    if amount_paid >= total_due:
        change = amount_paid - total_due
        print(f"Change Due: ${change:.2f}")
    else:
        balance = total_due - amount_paid
        print(f"Remaining balance to be paid: ${balance:.2f}")

# Testing display_mailing_label
print("--- Label 1 ---")
display_mailing_label('Luis Alicea', '123 Astoria la', 'Ashton', 'MD', '20961')
print("--- Label 2 ---")
display_mailing_label('River Ringling', '346 Paradis blv', 'Rockville', 'MD', '20882')

print('\n')

#Testing add_numbers
add_numbers(5)
add_numbers(10, 20)
add_numbers(3, 6, 9, 12, 15)

print('\n')

#Testing display receipt
print("--- Overpay ---")
display_receipt(50.00, 60.00)
print("--- Exact ---")
display_receipt(50.00, 50.00)
print("--- Underpay ---")
display_receipt(50.00, 30.00)