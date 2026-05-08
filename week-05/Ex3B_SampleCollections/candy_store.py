# Candy Store

# two tuples
candies = ('gummies', 'hard candy', 'taffy')
flavors = ('banana', 'strawberry', 'orange')

# Create a set of combinations
candy_options = set()
candy_options.add(candies[0] + ' - ' + flavors[1])
candy_options.add(candies[2] + ' - ' + flavors[0])
candy_options.add(candies[1] + ' - ' + flavors[2])
print("Today's candy options include: ")
print(candy_options)

# Sets are unordered and print in different orders.
