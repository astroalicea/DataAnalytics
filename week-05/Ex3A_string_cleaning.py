# String cleaning 

name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

# Using .lower() 

print(name_1.lower()) 
print(name_2.lower())
print(name_3.lower())

# Using .title()

print(name_1.title()) 
print(name_2.title())
print(name_3.title())

#  Using .replace()

print(salary_1.replace("$", "")) 
print(salary_2.replace("$", ""))

# Chaining .replace() and .int()
print(type(int(salary_1.replace("$", "").replace(",",""))))
