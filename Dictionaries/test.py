# # # # alien_0 = {
# # # #     'color':"red",
# # # #     'points': 5
# # # # }

# # # # print(alien_0['color'])
# # # # print(alien_0['points'])

# # # # alien_0['x_position'] = 0
# # # # alien_0['y_position'] = 25

# # # # print(alien_0)

# # # # users = {}

# # # # users['name'] = 'Elvis'
# # # # users['age'] = 26
# # # # users['skin_color'] = 'dark'

# # # # print(users)

# # # # del users['skin_color']
# # # # print(users)

# # # # movies = {
# # # #     'id':"isb16725627",
# # # #     'name': 'House of cards',
# # # #     'genre': "SciFi",
# # # #     'location': 'Netflix'
# # # # }

# # # # for movie_key in movies.keys():
# # # #     print(movie_key)

# # # # Try it yourself exercise 6:4
# # # glossary = {
# # #     'Boolean': 'True or False statements',
# # #     'Variables': 'Containers',
# # #     'String': 'Series of characters',
# # #     'Data_type': 'data values of an entity',
# # #     'List': 'Collection of items',
# # #     'Conditionals': 'logical statements',
# # #     'Objects': 'Non-primitive data type',
# # #     'Functions': 'Program that performs a specific task',
# # #     'Testing': 'Testing once program to see if its free from bugs',
# # #     'Inputs': 'Accepting data from user',
# # # }

# # # # for glossary_key, value in glossary.items():
# # # #     print(f"{glossary_key}: {value}")

# # # # 6.5
# # # rivers = {
# # #     'nile':'Egypt',
# # #     'niger': 'Nigeria',
# # #     'missisipi': 'USA'
# # # }

# # # for river, location in rivers.items():
# # #     print(f"The {river} runs through {location}")

# # # for river in rivers.keys():
# # #     print(f"{river}")

# # # for river_location in rivers.values():
# # #     print(f"The river location:{river_location}")

# # # # 6.6
# # # favorite_languages = {
# # #     'jen': 'python',
# # #     'sarah': 'c',
# # #     'edward': 'ruby',
# # #     'phil': 'python', 
# # #     }

# # # names = ['John', 'Sarah', 'Edward', 'Kelvin', 'Jonathan', 'Micheal']

# # # for name in names:
# # #     if name in favorite_languages.keys():
# # #         print(f"Thank you {name} for taking the poll")
# # #     else:
# # #         print(f"Hello, {name} please take the poll")    


# # # Chapter
# # # message = input("Tell me something: ")
# # # print(message)

# # # Multiple prompts
# # # prompt = "If you tell us who you are, we can personalize the messages you see."
# # # prompt += "\nWhat is your first name? "

# # # name = input(prompt)
# # # print(f"Hello, {name}")

# # # age = input("How old are you? ")
# # # message = f"I am {age} years old"
# # # print(message)

# # # Algorithm
# # # prompt = "Enter a number and I will let you know if it is even or odd: "

# # # number = int(input(prompt))

# # # if number % 2 == 0:
# # #     print(f"{number} is even")
# # # else:
# # #     print(f"{number} is odd")


# # # counter = 1

# # # while counter <= 10:
# # #     print(counter)
# # #     counter += 1

# # # active = True

# # # while active:
# # #     name = input("What is your name: ")

# # #     if name == 'Elvis':
# # #         active = False
# # #     else:
# # #         print(name)

# # # current_num = 0

# # # while current_num < 10:
# # #     current_num += 1

# # #     if current_num % 2 == 0:
# # #         continue

# # #     print(current_num)

# # prompt = "Tell me your age and I will let you know the cost of the movie ticket"
# # prompt += "Enter 'q' or 'Q' to exit the app: "

# # while True:
# #     age_prompt = input(prompt)

# #     if age_prompt == 'q' or age_prompt == 'Q':
# #         print("Logout....")
# #         break
# #     age_prompt = int(age_prompt)
# #     if age_prompt < 3:
# #         print('Your movie ticket is free')
# #         break
# #     elif age_prompt <=3 or age_prompt <=12:
# #         ticket = 10
# #         print(f"Your movie ticket costs ${ticket}")
# #         break
# #     else:
# #         ticket = 15
# #         print(f"Your movie ticket costs ${ticket}")
# #         break
        
# # unconfirmed_users = ['Janet', 'Mike', 'Nate']
# # confirmed_user = []

# # while unconfirmed_users:
# #     current_user = unconfirmed_users.pop()

# #     print(f"Verifying user: {current_user.title()}")
# #     confirmed_user.append(current_user)


# # # Display all confirmed users
# # for confirmed in confirmed_user:
# #     print(confirmed.title())

# # pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# # print(pets)

# # for pet in pets:
# #     if pet == 'cat':
# #         pets.remove('cat')

# # print(pets)

# # responses = {}
# # gen_counts = 0
# # all_values = []

# # polling_active = True

# # while polling_active:
# #     name = input("What is your name: ")
# #     favorite_city = input("What is your favorite city: ")

# #     responses[name] = favorite_city

# #     # Append all the cities
# #     all_values.append(favorite_city)
    
# #     # Count the number of people that took the poll
# #     gen_counts += 1

# #     repeat_poll = input("Would you let another person respond (yes/no): ")
# #     if repeat_poll == 'no':
# #         polling_active = False

# # print("\n--- Poll Results ---")
# # print(f"Number of people that took the poll: {gen_counts}")
# # for name, favorite_city in responses.items():
# #     print(f"{name}: {favorite_city}")

# # print("\nBelow is the number of cities selected by people who took the poll ")
# # for city_count in set(all_values):
# #     x = all_values.count(city_count)
# #     print(f"{city_count}:{x}")


# # Chapter 8
# def greet_user():
#     """Display a simple greeting"""
#     print("Hello, Elvis")

# greet_user()

# def greet_name(username):
#     """"Display a simple greeting to user"""
#     print(f"Hello, {username} how are you doing?")

# # greet_name('Elvis')

# def describe_city(city_name, country='Canada'):
#     """Describe a city"""
#     print(f"{city_name} is in {country}")


# describe_city('New york', 'USA')
# describe_city('San franicsco')
# describe_city('New Orleans')
# describe_city('Nova Scotia')

# Return Values in Functions







