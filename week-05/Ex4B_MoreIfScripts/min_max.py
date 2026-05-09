# Display the smallest and largest of three numbers using if/else statements

a = 45
b = 12
c = 78

if a > b and a > c:
    print(f"The largest number is {a}")
elif b > a and b > c:
    print(f"The largest number is {b}")
elif c > a and c > b:
    print(f"The largest number is {c}")

if a < b and a < c:
    print(f"The smallest number is {a}")
elif b < a and b < c:
    print(f"The smallest number is {b}")
elif c < a and c < b:
    print(f"The smallest number is {c}")