# 5.3 Alien Colors
# A program to test the value of the variable and assign points
# alien_color = "green"

#If logic
# if alien_color == 'green':
#     print("Player has earned 5 points")

# Test passed
# if alien_color == 'green':
#     print(alien_color == 'green', "Test passed")

# Test failed
# if alien_color != "green":
#     print(alien_color != "green")

# 5.4
# if-elif chain
# alien_colors = "red"
# if alien_colors == "green":
#     print("Player has earned 5 points")
# elif alien_colors != "green":
#     print("Player has earned 10 points")

# if-else chain
# if alien_colors == "green":
#     print("player has earned 5 points")
# else:
#     print("Player has earned 10 points")

# 5.5
# if alien_colors == "green":
#     points = 5
#     print(f"Player earned {points} points")
# elif alien_colors == "yellow":
#     points = 10
#     print(f"Player earned {points} points")
# else:
#     points = 15
#     print(f"Player earned {points} points")

# 5.6
# age = 14
# if age < 2:
#     print("You're a baby")
# elif age >= 2 and age < 4:
#     print("You a toddler")
# elif age >= 4 and age < 13:
#     print("You are a kid")
# elif age >= 13 and age < 20:
#     print("You are a teenager")
# elif age >= 20 and age < 65:
#     print("You are an adult")
# else:
#     print("You are an elder")


# 5.7
# favorite_fruits = ["apple", "orange", "banana", "avocado", "pear", "almond"]

# check whether item is in list
# if "gauva" in favorite_fruits:
#     print("You really like gauva")
# if "banana" in favorite_fruits:
#     print("You really like bananas")
# if "apple" in favorite_fruits:
#     print("You really like apple")
# if "mango" in favorite_fruits:
#     print("You really like mangoes")
# if "orange" in favorite_fruits:
#     print("You really like oranges")

# 5.8
# usernames = ['moment47', 'admin', 'vermic49', 'babs12', 'elv35']
# usernames = ['Vermic49']

# for username in usernames:
#     if username == 'admin':
#         print(f"Hello {username}, would you like to see a status report?")
#     else:
#         print(f"Hello {username},thank you for logging in again")

# # 5.9
# if usernames:
#     for username in usernames:
#         print(f"Hello {username}, how are you doing?")
# else:
#     print("\nWe need to find some users!")

# 5.10
current_users = ['Vermic1', 'Viktok133', 'titan32', 'mike32','opius44']
new_users = ['cody32', 'virus33', 'TITAN32', 'Opius44', 'melvin3']

current_users_mod = [] 
for user in current_users:
    current_users_mod.append(user.lower())

print(current_users_mod)
    
# Algorithm
for new_user in new_users:
    if new_user.lower() in current_users_mod:
        print(f'Please enter a new username, {new_user} not available')
    else:
        print(f"{new_user} username is available")

# 5.11
# num_list = [1, 2, 3 , 4, 5, 6, 7, 8, 9]

# for num in num_list:
#     if num == 1:
#         ordinal = "st"
#         print(f"{num}{ordinal}")
#     elif num == 2:
#         ordinal = "nd"
#         print(f"{num}{ordinal}")
#     elif num == 3:
#         ordinal = "rd"
#         print(f"{num}{ordinal}")
#     else:
#         ordinal = "th"
#         print(f"{num}{ordinal}")