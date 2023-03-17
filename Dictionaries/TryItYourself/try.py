# 6.1
# person = {
#     'first_name': 'Tosin',
#     'last_name': 'Babatunde',
#     'city': 'Lagos',
# }
# print(person['first_name'])
# print(person['last_name'])
# print(person['city'])

# # 6.2
# favorite_number ={
#     'Elvis': 6,
#     'Tosin': 7,
#     'Ada': 5,
#     'Bob': 4,
#     'Kelvin': 63,
# }

# fav_el = favorite_number['Elvis']
# fav_to = favorite_number['Tosin']
# fav_ad = favorite_number['Ada']
# fav_bo = favorite_number['Bob']
# fav_ke = favorite_number['Kelvin']
# print(f"Elvis favourite number is {fav_el}")
# print(f"Tosin favourite number is {fav_to}")
# print(f"Ada favourite number is {fav_ad}")
# print(f"Bob favourite number is {fav_bo}")
# print(f"Kelvin favourite number is {fav_ke}")

# # 6.3
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

# print(f"Boolean: {glossary['Boolean']}")
# print(f"Variables: {glossary['Variables']}")
# print(f"String: {glossary['String']}")
# print(f"Data_type: {glossary['Data_type']}")
# print(f"List: {glossary['List']}")

# 6.4
# Adding aa for loop to the above program
# for term, definition in glossary.items():
#     print(f"{term.title()}: {definition.title()}")

# 6.5 Rivers
rivers = {
    'nile': 'egypt',
    'niger': 'Nigeria',
    'mississippi': 'USA',
}

# for river_name, location in rivers.items():
#     print(f"The {river_name.title()} runs through {location.title()}")

# Print the name of the rivers only
# for river_name in rivers.keys():
#     print(f"{river_name}")

# Print the name of the country only
# for river_location in rivers.values():
#     print(f"The location of river is: {river_location}")

# 6.6
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python', 
#     }

# names_list = ['jen', 'kelvin', 'edward', 'jonas', 'phil', 'martins']

# for name in names_list:
#     if name in favorite_languages.keys():
#         print(f"Thank you {name} for taking the poll")
#     else:
#         print(f"Hello {name}, Please you are invited to take the poll")

# 6.7 People
# Create a dict of 3 persons
person_0 = {
    'first_name': 'Tosin',
    'last_name': 'Babatunde',
    'city': 'Lagos',
}
person_1 = {
    'first_name': 'Mike',
    'last_name': 'John',
    'city': 'Canada',
}
person_2 = {
    'first_name': 'Jane',
    'last_name': 'Doe',
    'city': 'USA',
}
# Make a list to store people
# people = [person_0, person_1, person_2]

# for person in people:
#     fullname = f"{person['first_name']} {person['last_name']}"
#     location = f"{person['city']}"

#     print(f"\nFullname: {fullname.title()}")
#     print(f"City: {location.title()}")

# 6.8
# dog = {
#     'name': 'Rally',
#     'owner': 'Ben',
# }
# cat = {
#     'name': 'miky',
#     'owner': 'John',
# }
# sheep = {
#     'name': 'kenny',
#     'owner': 'Jane',
# }
# chicks = {
#     'name': 'cocky',
#     'owner': 'Denver',
# }
# Store the dictionary into a list
pets = []

# Check for the list is empty
# if pets:
#     print("List is not empty")
# else:
    # Append all the dict to the list
    # pets.append(dog)
    # pets.append(cat)
    # pets.append(sheep)
    # pets.append(chicks)

# Then loop through the list and print out the items
# for pet_name in pets:
#     print(f"\nPet_name: {pet_name['name']}")
#     print(f"Owner_name: {pet_name['owner']}")

# 6.9 Favorite Places
# favorite_places = {
#     'Elvis':['Canada', 'Italy', 'Norway'],
#     'Martin':['USA', 'Germany', 'Austria'],
#     'Dave':['Qatar', 'Rwanda', 'Congo'],
# }
# # Loop through the dictionary
# for person, cities in favorite_places.items():
#     print(f"\n{person}'s favorite places are: ")
#     for city in cities:
#         print(f"{city}")

# 6.10 Favorite Numbers
# favorite_number ={
#     'Elvis': [6, 8],
#     'Tosin': [7, 9, 10],
#     'Ada': [5, 3, 6],
#     'Bob': [4, 15],
#     'Kelvin': [63, 125],
# }
# Loop through the dictionary
# for name, favs_num in favorite_number.items():
#     print(f"\n{name}'s favorite number are: ")
#     for fav_num in favs_num:
#         print(f"\t{fav_num}")

# 6.11 Cities
# cities = {
#     'toronto':{
#         'country': 'canada',
#         'population': 7842430223,
#         'fact': 'Most populus country'
#     },
#     'Syndey':{
#         'country': 'Austrialia',
#         'population': 32430223,
#         'fact': 'Tourist site for lovers'
#     },
#     'New-york':{
#         'country': 'USA',
#         'population': 132430223,
#         'fact': 'Most travelled destination for academics'
#     },
# }

# for city_name, city_info in cities.items():
#     print(f"\nThese are the various info about the city: {city_name}")
#     country = city_info['country']
#     population = city_info['population']
#     fact = city_info['fact']
#     print(f"Country: {country}")
#     print(f"Population: {population}")
#     print(f"Fact: {fact}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python', 
}
# Set counter variable
count = 0
python_list = []
# Loop through the dictionary
for name, language in favorite_languages.items():
    if language == 'python':
        count += 1
        python_list.append(name)
        print(f"{name.title()} : {language}")
    else:
        print(f"{name} : {language}")
#The Total number of people that choose python program 
print(f"The number of people that choose {language} are: {count}")
print(f'The list of people that took python are: {python_list}')
