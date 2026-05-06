#  Calculating tours 
import math

tourists = 38

vans_needed = math.ceil(tourists / 15)
# print(vans_needed)
total_cost = vans_needed * 250
# print(total_cost)
cost_per_person = total_cost / tourists
# print(cost_per_person)

print(f"Number of tourists: {tourists}")
print(f"Vans needed: {vans_needed}")
print(f"Total cost: ${total_cost}")
print(f"Cost per person: ${cost_per_person:.2f}")

# There is 28 cents leftover because we have round up for the seating space. 
# There cant be a half a person on a van