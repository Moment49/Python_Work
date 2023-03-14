# Checking Whether a Value is in a List
# requested_toppings = ['mushroom', 'onions', 'pineapple']
# if 'mushroom' in requested_toppings:
#     print(True)
# if 'pepperoni' in requested_toppings:
#     print(False)
# else:
#     print(False)

#Checking whether an item is not in a list
# banned_users = ['andrew', 'carolina', 'david']
# user = 'marie'

# if user not in banned_users:
#     print(f"{user.title()}, you can post a response if you wish.")

#Simple If Statements
# age = 19
# if age >= 18:
#     print('You are old enough to vote')
#     print("Have you registered to vote yet?")
# else:
#     print("Sorry you are too young to vote")
#     print("Please register to vote as soon as you turn 18!")

# if-elif-else chain
# age = 66

# if age < 4:
#     price = 0
# elif age >= 4 and age < 18:
#     price = 25
# elif age < 65:
#     price = 40
# elif age >= 65:
#     price = 20

# print(f'Your admission cost is ${price}')

# Testing Multiple Conditions
# requested_toppings = ['mushrooms', 'extra cheese']

# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms")
# if 'pepperoni' in requested_toppings:
#     print('Adding pepperoni')
# if 'extra cheese' in requested_toppings:
#     print('Adding extra cheese')

# print("\nFinished making your pizza")

# IF statements with Lists
# requested_toppings = ['mushrooms', 'extra cheese', 'green peppers']


# for requested_topping in requested_toppings:
#     if requested_topping ==  "green peppers":
#         print("Sorry, we are out of green peppers right now.")
#     else:
#         print(f"Adding {requested_topping}.")

# print("\nFinished making your pizza!")

# Checking that a list is not empty
# requested_toppings = []

# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}")
#     print("\nFinished making your pizza")
# else:
#     print("Are you sure you want a plain pizza?")

# Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 
                      'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# Alogrithm
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we dont have {requested_topping}")

print("\nFinished maaking your pizza")