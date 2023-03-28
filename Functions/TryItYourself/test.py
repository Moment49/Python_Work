# 8.1 Message
# def display_message(course):
#     """Display message to the users"""
#     print(f"I am learning {course} programming")

# display_message('python')

# # 8.2Favorite Book:
# def favorite_book(title):
#     """A function to display my favorite book"""
#     print(f"\nOne of my favorite books is {title}")

# favorite_book('Alice in wonderland')

# 8.3
# def make_shirt(text, size='Large'):
#     """Display the shirt size and text message"""
#     print(f"the shirt size is {size} and the message on the shirt is {text}")

# # make_shirt('Medium', 'I love Python')
# make_shirt('I love Python')
# make_shirt(size='Large', text='Eden')

# 8.4
# def make_shirt(text, size='Large'):
#     """Display the shirt size and text message"""
#     print(f"the shirt size is {size} and the message on the shirt is {text}")

# # make_shirt('Medium', 'I love Python')
# make_shirt('I love Python')
# make_shirt('I love coding', size='Small')

# 8.5
# def describe_city(city, country):
#     """Display city name and country"""
#     print(f"{city.title()} is in {country.title()}")

# describe_city("toronto", "canada")

# 8.6 
# def city_country(city, country):
#     """Return the formatted city and country"""
#     country_info = f"{city.title()}, {country.title()}"
#     return country_info

# Country = city_country('ontario', 'canada')
# print(Country)
# Country2 = city_country(country='USA', city='Chicago')
# print(Country2)
# Country3 = city_country('dublin', 'Ireland')
# print(Country3)

# 8.7 8.8
# def make_album(artist_name, album_title, songs=None):
#     """Return a dict of musicians"""
#     music_profile = {'artist': artist_name, 'album':album_title}
#     if songs:
#         music_profile['songs'] = songs
#     return music_profile

# # Write a program to accept user input
# print("\nPlease share your favorite album & artist")
# print("Enter 'q' or 'quit' anytime to exit" )
# Ispolling = True
# while Ispolling:
#     # Get artist name Input from user
#     artist = input("Enter name of artist: ")

#     # Condition to exit loop
#     if artist == 'q' or artist == 'quit':
#         break
        
#     #Get title input from user
#     title = input("Enter album title: ")

#     # Condition to exit loop
#     if title == 'q' or title == 'quit':
#         break
#     music_record = make_album(artist, title)
#     print(music_record)



# music_record1 = make_album('Don meon', 'Awesome God', songs=36)
# print(music_record1)
# music_record2 = make_album('moses bliss', 'too faithful')
# print(music_record2)
# music_record3 = make_album('Mercy Chinwo', 'Obinasom')
# print(music_record3)

# 8.9
# def show_messages(messages):
#     """Display series of messages"""
#     for message in messages:
#         print(message)

# messages = ['welcome everyone', 'I love God', 'Thank Jesus', 'Awesome God']
# show_messages(messages)  

# 8.10 8.11
# def send_messages(print_messages, sent_messages):
#     """Display the messages in the list"""
#     print("\nList of messages printed: ")
#     while print_messages:
#         pop_msg = print_messages.pop()
#         print(f"List of msg printed: {pop_msg}")
#         # Move each message to a new list
#         sent_messages.append(pop_msg)
#     return f"This is the Internal List modified{print_messages}"

# def show_messages(sent_messages):
#     """Show the printed message"""
#     print("\nThis is a list of sent message:")
#     for sent_message in sent_messages:
#         print(sent_message)
#     # return sent_messages

# messages = ['welcome everyone', 'I love God', 'Thank Jesus', 'Awesome God']
# sent_messages = []

# modified_msg = send_messages(messages[:], sent_messages)
# print(modified_msg)

# show_messages(sent_messages)

# print(f"\nThis is my original list{messages}")
# print(f"This is the sent messages List {sent_messages}")

#  8.12
# def build_sandwich(*items):
#     """Display the items on a sandwich"""
#     print("\nMaking your delicious sandwich bite")
#     # Convert to a list
#     list(items)
#     # Iterate over the items and print each item
#     for item in items:
#         print(f"- {item}")

# build_sandwich('Pepperoni', 'talita', 'bacon', 'carrot', 'cheese')
# build_sandwich('haznut', 'cuba', 'mozerella')
# build_sandwich('cabbage', 'chille', 'veges')

# 8.13
# def build_profile(first, last, **user_info):
#     """Build a dict containing everything we know about a user"""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# user_profile = build_profile('albert', 'einstein', 
#                              location='princeton', field='physics')

# print(user_profile)

# user_profile2 = build_profile('Elvis', 'Ibenacho', 
#                               location = 'Lagos', field = 'Data science', 
#                               hobby = 'football')
# print(user_profile2)

# 8.14
def build_car(manufacturer, model, **car_info):
    """Return a dictionary info of a car"""
    # Store the manufacrurer and model name in the dict(car_info)
    car_info['manufacturer_name'] = manufacturer
    car_info['model_name'] = model
    return car_info

car = build_car('subaru', 'outback', color='blue', tow_package=True)
print(car)