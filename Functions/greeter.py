# Passing Information to a function
# def greet_user(username):
#     """_Display a simple greeting_"""
#     print(f"Hello! {username}")

# greet_user('Elvis')

#Positional Arguments
# def describe_pet(animal_type, pet_name):
#     """Display information about a pet"""
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}")

# describe_pet('cat', 'candy')
# describe_pet('dog', pet_name='bruno')

#Default Values
# def describe_pet(pet_name, animal_type='dog'):
# #     """Display information about a pet"""
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}")

# describe_pet('candy', 'cat')
# # describe_pet(pet_name='bruno')
# describe_pet('bruno')

# Avoiding Argument Errors
# Calling the function describe pets with no arguments
# def describe_pet(pet_name, animal_type='dog'):
#     """Display information about a pet"""
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}")


# describe_pet()

# Return Values
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatky formatted"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# Making an Argument Optional
# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Return a full name, neatky formatted"""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"

#     return full_name.title()

# musician = get_formatted_name('john','hooker', 'lee')
# print(musician)

# musician = get_formatted_name('john','hooker')
# print(musician)

# Returning a Dictionary
# def build_person(first_name, last_name, age=None):
#     """Return a dict of Info about a person"""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person

# programmer = build_person('Elvis', 'Ibenacho', age=47)
# print(programmer)

# Function with a While Loop
# def build_person(first_name, last_name):
#     """Return a full_name"""
#     full_name = f"{first_name} {last_name}"
#     return full_name


# while True:
#     "# Accept user Input"
#     print("\nPlease tell me your name")
#     print("Enter q to quit program")

#     f_name = input("Enter your first name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Enter your last name: ")
#     if l_name == 'q':
#         break
#     # Condition to test each full name
#     Formatted_name = build_person(f_name, l_name)
#     print(f"\nHello,{Formatted_name}")

# Paasing a List
# def greet_users(names):
#     """Print a simple greeting to each user in the list"""
#     for name in names:
#         msg = f"Hello, {name.title()}!"
#         print(msg)
# usernames = ['hannah', 'ty', 'target']
# greet_users(usernames)

# Start with some designs that need to be printed

# def print_models(unprinted_designs, completed_models):
#     """Simulate printing design until none is left.
#         Move each design to completed models after printing
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing Model: {current_design}")
#         # Appending the current design
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     """Display all completed modes"""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# 8.15 Printing Models
# import printing_func
# import printing_func as pf
# from printing_func import  print_models
# from printing_func import  print_models as pm
# from printing_func import  show_completed_models as sm
# from printing_func import  show_completed_models


# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# printing_func.print_models(unprinted_designs, completed_models)
# pf.print_models(unprinted_designs, completed_models)
# print_models(unprinted_designs, completed_models)
# pm(unprinted_designs, completed_models)
# show_completed_models(completed_models)
# sm(completed_models)
# printing_func.show_completed_models(completed_models)
# pf.show_completed_models(completed_models)


# Passing an Arbitrary Number of Arguments
# def make_pizza(size, *toppings):
#     """Summarize the pizza and print the list of toppings requested"""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")
# make_pizza(14, 'pepperoni')
# make_pizza(16, 'pepperoni', 'green peppers', 'extra cheese')

# Using Arbitrary Keyword Arguments
# def build_profile(first, last, **user_info):
#     """Build a dict containing everything we know about a user"""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# user_profile = build_profile('albert', 'einstein', 
#                              location='princeton', field='physics')

# print(user_profile)

# Importing an Entire Module

















