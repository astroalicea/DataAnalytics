import random

products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
            'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector']

#a) Product of thee Day - one random item
product_of_day = random.choice(products)
print(f"Product of the day: {product_of_day}")

#b) Usability survey - 3 items, no repeats
survey_items = random.sample(products, 3)
print(f"Survey products: {survey_items}")

#c) Randomized display order - shuffle in place
random.shuffle(products)
print(f"Randomized product list: {products}")

#d) Simulated daily transaction count
transactions = random.randint(50, 300)
print(f"Daily transaction count: {transactions}")
