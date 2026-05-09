# Complex taxes

pay_rate = float(input("Enter pay rate: "))
hours_worked = float(input("Enter hours worked: "))
gross_pay = 0

if hours_worked <= 40:
    gross_pay = hours_worked * pay_rate
   
else:
    regular_pay = 40 * pay_rate
    overtime_pay = (hours_worked - 40) * pay_rate * 1.5
    gross_pay = regular_pay + overtime_pay

print(f"Gross pay is: ${gross_pay:,.2f}")

annual_gross = gross_pay * 52 #52 weeks in a year
filing_status = input("Enter filing status (single/joint): ")

if filing_status == 'single':
    if annual_gross <12000:
        tax_rate = .05
    elif annual_gross < 25000:
        tax_rate = .10
    elif annual_gross < 75000:
        tax_rate = .15
    else:
        tax_rate = .20


elif filing_status == 'joint':
    if annual_gross < 12000:
        tax_rate = .0
    elif annual_gross < 25000:
        tax_rate = .06
    elif annual_gross < 75000:
        tax_rate = .11
    else:
        tax_rate = .20

tax_withheld = gross_pay * tax_rate
net_pay = gross_pay - tax_withheld

print(f"You worked {hours_worked} hours this period.")
print(f"Because you earn ${pay_rate} per hour, your gross weekly pay is ${gross_pay:,.2f}")
print(f"Your filing status is {filing_status}")
print(f"Your tax withholding for the week is ${tax_withheld:,.2f}")
print(f"Your net pay is ${net_pay:,.2f}")
