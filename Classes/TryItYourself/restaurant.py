# 9.1
# class Restaurant:
#     """An attempt to model a restaurant"""
#     def __init__(self, restaurant_name, cuisine_type):
#         """Initialize the name and cuisine type of the restaurant"""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#     def describe_restaurant(self):
#         """Describe the restaurant"""
#         print(f"\nThe name of the restaurant is {self.restaurant_name}")
#         print(f"The sell a delicious {self.cuisine_type} cuisine")
#     def open_restaurant(self):
#         """Open the restaurant"""
#         print(f"The {self.restaurant_name} is now open")

# # restaurant = Restaurant('mega chicken', 'jollof rice')
# # print(f"Restaurant: {restaurant.restaurant_name}")
# # print(f"cuisine: {restaurant.cuisine_type}")
# # # Calling the methods
# # restaurant.describe_restaurant()
# # restaurant.open_restaurant()

# 9.6 Ice Cream Stand
# class IceCreamStand(Restaurant):
#     """Model of Ice cream stand"""
#     def __init__(self, restaurant_name, cuisine_type, *flavors):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = flavors
#     def show_flavors(self):
#         """Convert to a list before Showing flavors"""
#         Ice_flavors_list = list(self.flavors)
#         # for flavor in Ice_flavors_list:
#         #     print(flavor)
#         print(Ice_flavors_list)

# myIce = IceCreamStand('SuperBite', 'IceCreamShop', 
#                       'Vanilla', 'straberry', 'milk', 'cheese')
# myIce.show_flavors()
        


# 9.2
# my_restaurant = Restaurant('The place', 'fried rice')
# tosin_restaurant = Restaurant('jendol', 'dounuts')
# kelvin_restaurant = Restaurant('sweet sensation', 'meat pie')

# my_restaurant.describe_restaurant()
# tosin_restaurant.describe_restaurant()
# kelvin_restaurant.describe_restaurant()

# 9.3/9.5
# class User:
#     """A class to model a website user"""
#     def __init__(self, first_name, last_name, age):
#         """A model for a user"""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.login_attempts = 0
       
#     def describe_user(self, **user_info):
#         """Describe the user"""
#         self.user_info = user_info
#         user_info['first_name'] = self.first_name 
#         user_info['last_name'] = self.last_name 
#         user_info['age'] = self.age
#         return user_info
    
#     def greet_user(self):
#         """Greet the user"""
#         fullname = f"{self.first_name} {self.last_name}"
#         print(f"Welcome to Python, {fullname}")

#     def increment_login_attempts(self):
#         """Increment the login attempts"""
#         self.login_attempts += 1
#         print(self.login_attempts)

#     def reset_login_attempt(self):
#         """Reset the login attempt"""
#         if self.login_attempts > 0:
#             self.login_attempts = 0
#             print(self.login_attempts)

# model_user = User('Elvis', 'Ibenacho', age=26)
# model_user2 = User('Tosin', 'Babatunde', age=27)
# model_user3 = User('Cassy', 'Temi', age=30)
# model_user.increment_login_attempts()
# model_user.increment_login_attempts()
# model_user.increment_login_attempts()

# print(f"Login attempts: {model_user.login_attempts}")
# model_user.reset_login_attempt()
# print(f"Login attempts: {model_user.login_attempts}")

# model_user_dict = model_user.describe_user()
# model_user_dict2 = model_user2.describe_user()
# model_user_dict3 = model_user3.describe_user()
# # Print out user Information
# for key, value in model_user_dict.items():
#     print(f"{key} : {value}")
# print(model_user_dict)
# print(model_user_dict2)
# print(model_user_dict3)
# # Call the greet_user method(To greet user)
# model_user.greet_user()
# model_user2.greet_user()
# model_user3.greet_user()

# 9.8 Privileges
# class Privileges:
#     """An attempt to assign privileges for a super user"""
#     def __init__(self, *privileges):
#         self.privileges = privileges

#     def show_privileges(self):
#         """Show list of Admin privileges"""
#         print('This is the list of Admin rights: ')
#         for privilege in self.privileges:
#             print(privilege)

# # 9.7 Admin
# class Admin(User):
#     """Attempt to model an admin user of a website"""
#     def __init__(self, first_name, last_name, age):
#         super().__init__(first_name, last_name, age)
#         self.privileges = Privileges("can add post", "can delete post", "can ban user")
        
 

# admin_user = User('Elvis', 'Ibenacho', age=26)
# admin_user = Admin('Elvis', 'Ibenacho', 27, 'can add post', 'can delete post', 'can ban user')
# admin_user.show_privileges()
# print(admin_user.describe_user())

# admin_user_1 = Admin("Kelvin", 'Martin', 24)
# admin_user_1.privileges.show_privileges()
# print(admin_user_1.describe_user())

# #9.4
# class Restaurant:
#     """An attempt to model a restaurant"""
#     def __init__(self, restaurant_name, cuisine_type):
#         """Initialize the name and cuisine type of the restaurant"""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 23
#     def describe_restaurant(self):
#         """Describe the restaurant"""
#         print(f"\nThe name of the restaurant is {self.restaurant_name}")
#         print(f"The sell a delicious {self.cuisine_type} cuisine")
#     def open_restaurant(self):
#         """Open the restaurant"""
#         print(f"The {self.restaurant_name} is now open")
#         print(f"The restaurant has served {self.number_served} customers")

#     def set_number_served(self, num_served):
#         """Add the number of customers served"""
#         if num_served >= self.number_served:
#             self.number_served = num_served
#         else:
#             print('We cant serve again')
#     def increment_number_served(self, increment_serves):
#         """Increment the number of customers been served"""
#         self.number_served += increment_serves

# restaurant = Restaurant('mega chicken', 'jollof rice')
# # print(f"The restaurant has served {restaurant.number_served} customers")
# restaurant.set_number_served(46)
# restaurant.increment_number_served(100)
# restaurant.open_restaurant()

# print(f"Restaurant: {restaurant.restaurant_name}")
# print(f"cuisine: {restaurant.cuisine_type}")
# # Calling the methods
# restaurant.describe_restaurant()
# restaurant.open_restaurant()    

# 9.9 Battery Upgrade
# class Car:
#     """A simple attempt to represent a car."""

#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
    
#     def get_descriptive_name(self):
#         """Return neatly formatted descriptive name"""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         """Print a statement showing the car's mileage"""
#         print(f"This car has {self.odometer_reading} miles on it.")

#     # Modifying an Attribute's value through a method
#     def update_odometer(self, mileage):
#         """Set the odometer reading to a given value
#             and reject change if it attempts to roll the odometer back 
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer")

#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading"""
#         self.odometer_reading += miles

# #Instance as Attributes
# class Battery:
#     """A simple attempt to model a battery for an electric car."""
#     def __init__(self, battery_size = 85):
#         """Initialize the battery attributes"""
#         self.battery_size = battery_size

#     def describe_battery(self):
#         """Print a statement describing the battery size."""    
#         print(f"This car has a {self.battery_size}-kwh battery.")
    
#     def get_range(self):
#         """Print a statement about the range this battery provides"""
#         if self.battery_size == 85:
#             range = 260
#         elif self.battery_size == 100:
#             range = 315

#         print(f"This car can go about {range} miles on full charge.")

#     def upgrade_battery(self):
#         """Upgrade the car battery and check if the battery size 
#             is set to 100
#         """
#         if self.battery_size != 100 :
#             self.battery_size = 100
#             print(f"This is battery capacity {self.battery_size}")
#             print("Updgrade the battery capacity")
#         else:
#             print("Battery is already upgraded")
#             return -1
        
# # Defining Attributes and methods for the child class
# class ElecricCar(Car):
#     """Represents aspects of a car, specific to electric vehicles"""

#     def __init__(self, make, model, year):
#         """Initialize attributes of a car specific to electric vehicles"""
#         super().__init__(make, model, year)
#         self.battery = Battery()

# my_telsa2 = ElecricCar('tesla', 'model s', 2023 )        
# print(my_telsa2.get_descriptive_name())
# my_telsa2.battery.describe_battery()
# my_telsa2.battery.get_range()
# my_telsa2.battery.upgrade_battery()
# my_telsa2.battery.get_range()




# Random Module
from random import randint
from random import choice

# rand_num = randint(1, 10)
# print(rand_num)

# players = ['charles', 'martina', 'micheal', 'florence', 'eli']
# first_up = choice(players)
# print(first_up)

# 9.13
class Dice:
    """An attempt to model a dice roll"""
    def __init__(self, sides=6):
        """Initilaize a dice with sides"""
        self.sides = sides

    def roll_dice(self):
        """Roll the dice once using the random method"""
        # Create an empty list to hold all rolled dice
        rolled_num = []
        for value in range(1, 11):
            rand_num = randint(1, self.sides)
            rolled_num.append(rand_num)
        return rolled_num

# 6 sided dice and roll 10 times
roll_6 = Dice()
print(roll_6.roll_dice())

# 10 sided dice and 10 rolles
roll_10 = Dice(10)
print(roll_10.roll_dice())    

# 20 sided and roll 10times
roll_20 = Dice(20)
print(roll_20.roll_dice())


# 9.14 Lottery / Lottery analysis
# A function to generate a random ticket
def random_numbers(lottery_numbers):
    """Get a ticket of four numbers and store in a list"""
    wining_ticket = []
    for idx in range(4):
        lottery = choice(lottery_numbers)    
        # Checking if the lottery number is already in ticket else generate
        # another number
        if lottery in wining_ticket:
            # Generate another number
            lottery = choice(lottery_numbers)
        wining_ticket.append(lottery)
    return wining_ticket

def check_ticket(win_ticket, played_ticket):
    """"Check the ticket for a winner"""
    for element in played_ticket:
        if element not in win_ticket:
            return False
    return True

lottery_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
played_ticket = [3, 'A', 'B', 4]
win_ticket = random_numbers(lottery_nums)

# Check for a wining ticket  
check_ticket(win_ticket, played_ticket)


won = False
plays = 0
max_tries = 1_000_000

while not won:
    # get random ticket
    win_ticket = random_numbers(lottery_nums)
    won = check_ticket(win_ticket, played_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print('This is my lottery wining ticket')
    print(f"my ticket {played_ticket}")  
    print(f"Wining ticket: {win_ticket}")
    print(f'It took {plays} to win')
else:
    print(f"Tried {plays} times without pulling a winner")
    print(f"Played ticket: {played_ticket}")
    print(f"Win ticket: {win_ticket}")
























