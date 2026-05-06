# Tip amount

steak_frites = 30
braised_lamb = 25
octopus = 20
churros = 7
bottle_of_wine = 21

bill_total = steak_frites + braised_lamb + octopus + churros + bottle_of_wine
print(f"Bill without tip: {bill_total}")

tip_percentage = .20

tip_amount = bill_total * tip_percentage
print(f"The tip on a ${bill_total:.2f} restaurant bill is ${tip_amount:.2f}")


