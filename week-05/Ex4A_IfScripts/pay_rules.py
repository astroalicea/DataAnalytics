# Calcuulate gross pay

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