# Greeting display based on current hour

current_hour = int(input("Enter only the hour: "))


if current_hour < 10:
    print("Good morning!")
elif current_hour < 17:
    print("Good day!")
else:
    print("Good evening!")

# Additional late night check
if current_hour  >= 23 or current_hour <= 4:
    print("What are you doing up so late?")
    
