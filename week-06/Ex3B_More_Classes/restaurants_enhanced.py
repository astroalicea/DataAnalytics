class Restaurant:
    """
    This class represents a restaurant with a name and food type, number of customers served,
    and customer ratings.
    """

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")
    
    def add_num_served(self):
        served = int(input("How many customers served today? "))
        self.number_served += served

    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers.")

    def customer_rating(self):
        while True:
            rating = input("How would you rate your experience today on a scale of 1-5? ")
            if rating.isdigit() and 1 <= int (rating) <= 5:
                rating = int(rating)
                self.customer_ratings.append(rating)
                avg = sum(self.customer_ratings) / len(self.customer_ratings)
                print(f"Your rating was {rating}. the average rating for {self.rest_name} is {avg:.1f}")
                break
            else:
                print("Invalid input Please enter a whole number between 1 and 5.")

#Create three instances
rest1 = Restaurant('Sopranos', 'Italian')
rest2 = Restaurant('Dragon Palace', 'Chinese')
rest3 = Restaurant('Jiros sushi', 'Japanese')

#Call both methods for each instance
rest1.describe_rest()
rest1.rest_open()

rest2.describe_rest()
rest2.rest_open()

rest3.describe_rest()
rest3.rest_open()

#Test print_num_served and add_num_served
rest1.print_num_served()
rest1.add_num_served()
rest1.add_num_served()
rest1.print_num_served()

print()


#Test customer_rating
rest1.customer_rating()
rest1.customer_rating()
rest1.customer_rating()

#Test rest2
rest2.print_num_served()
rest2.add_num_served()
rest2.add_num_served()
rest2.print_num_served()

print()


#Test customer_rating rest2
rest2.customer_rating()
rest2.customer_rating()
rest2.customer_rating()


#Test rest3
rest3.print_num_served()
rest3.add_num_served()
rest3.add_num_served()
rest3.print_num_served()

print()


#Test customer_rating rest3
rest3.customer_rating()
rest3.customer_rating()
rest3.customer_rating()


