# alien_0 = {
#     'color':"red",
#     'points': 5
# }

# print(alien_0['color'])
# print(alien_0['points'])

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25

# print(alien_0)

# users = {}

# users['name'] = 'Elvis'
# users['age'] = 26
# users['skin_color'] = 'dark'

# print(users)

# del users['skin_color']
# print(users)

# movies = {
#     'id':"isb16725627",
#     'name': 'House of cards',
#     'genre': "SciFi",
#     'location': 'Netflix'
# }

# for movie_key in movies.keys():
#     print(movie_key)

# Try it yourself exercise 6:4
glossary = {
    'Boolean': 'True or False statements',
    'Variables': 'Containers',
    'String': 'Series of characters',
    'Data_type': 'data values of an entity',
    'List': 'Collection of items',
    'Conditionals': 'logical statements',
    'Objects': 'Non-primitive data type',
    'Functions': 'Program that performs a specific task',
    'Testing': 'Testing once program to see if its free from bugs',
    'Inputs': 'Accepting data from user',
}

# for glossary_key, value in glossary.items():
#     print(f"{glossary_key}: {value}")

# 6.5
rivers = {
    'nile':'Egypt',
    'niger': 'Nigeria',
    'missisipi': 'USA'
}

for river, location in rivers.items():
    print(f"The {river} runs through {location}")

for river in rivers.keys():
    print(f"{river}")

for river_location in rivers.values():
    print(f"The river location:{river_location}")