# alien_0 = {'color': 'green','points': 5}

# # print(alien_0['color'])
# # print(alien_0['points'])

# # Adding New Key-value pairs
# new_points = alien_0['points']
# print(f"You just earned {new_points} points")

# alien_0['position-x'] = 0
# alien_0['position-y'] = 25
# print(alien_0)

# Empty Dictionary
# alien_0 = {'color': 'green'}

# # alien_0['color'] = 'green'
# # alien_0['points'] = 5
# # print(alien_0)

# # Modifying values
# print(f"The alien is {alien_0['color']}")

# alien_0['color'] = 'yellow'
# print(f"The alien is now {alien_0['color']}")

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# alien_0['speed'] = 'medium'
# # Algorithm
# # Move the alien to the right.
# # Determine how far to move the alien based on its cureent speed
# if alien_0['speed'] == 'slow':
#     x_increment  = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     # Thi smust be a fast alien
#     x_increment = 3

# The new poistion is the old position plus the increment
# alien_0['x_position'] += x_increment
# print(f"New poisiton: {alien_0['x_position']}")

# Removing Key-value pairs
# alien_1 = {'color': 'red', 'points': 9}
# print(alien_1)

# del alien_1['color']
# print(alien_1)

# Dictionary of Similar Objects
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python', 
#     }
# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}")

# Using get() to Access Values
# alien = {'color': 'red', 'speed': 'slow'}
# point_value = alien.get('points', 'No point value assigned.')
# print(point_value)

# Looping through All key-Value Paira
# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
# }

# for key, value in user_0.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python', 
#     }

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}")

# Looping through all keys in a dictionary
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python', 
#     }

# friends = ['phil', 'sarah']
# # This code will loop through just the keys of the dict
# # for name in favorite_languages:
# for name in favorite_languages.keys(): 
#     print(name.title())

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")

# if 'erin' not in favorite_languages.keys():
#     print('Erin, please take our poll!')

# favorite_languages['erin'] = 'python'
# if 'erin' in favorite_languages.keys():
#     print('Thank you erin, for taking the poll ')

# Looping through a dict keys in a Partivuler Order
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python', 
#     }

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")

# # Looping Through all Values in a Dictionary
# print("\nThe following languages have been mentioned:")
# for language in set(favorite_languages.values()):
#     print(language.title())

# myset = {"C#", "python", "C++", "Java", "python"}
# print(myset)

#NESTING
# alien_0 = {'color': 'green', 'points':5}
# alien_1 = {'color': 'yellow', 'points':10}
# alien_2 = {'color': 'red', 'points':15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# Creating a fleet of aliens
aliens = []
for alien_num in range(30):
    alien_new = {'color': 'gold', 'points': 22, 'speed': 'fast'}
    # Append the new alien created to the aliens list
    aliens.append(alien_new)


for alien in aliens[:3]:
    if alien['color'] == 'gold':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show First 5 aliens
for alien in aliens[:5]:
    print(alien)
# Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")

# A list in a Dictionary
pizza ={
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese'],
}

# summarize the order
# print(f"You ordered a {pizza['crust']} crust pizza with the following toppings:")

# for topping in pizza['toppings']:
#     print("\t" + topping)

# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'javascript'],
#     'phil': ['python', 'go'], 
#     }

# for name, languages in favorite_languages.items():
#     print(f"\n{name.title()}'s favorite languages are: ")
#     for language in languages:
#         print(f"\t{language.title()}")

# A dictionary in a Dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },

}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

