# Federal tax calculator

salary = float(input("Enter monthy salary: "))

tax_withheld = salary * .23

print(f"Amount withheld for taxes is: ${tax_withheld:,.2f}")