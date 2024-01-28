# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# Writing Clear prompts
# name = input("Please enter your name: ")
# print(f"\nHello, {name}")

# Multiple prompts
# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "

# name = input(prompt)
# print(f"\nHello, {name}")

# Using Int() to Accept Numerical Input
# age = input("How old are you? ")
# # Convert the input string to integer
# age = int(age)
# print(age)

# height = int(input("How tall are you, in inches? "))

# if height >= 38:
#     print("\nYou're tall enough to ride")
# else:
#     print("\nYou'll be able to ride when you're a little older.")

# Modulo Operator
# number = int(input("Enter a number, and I'll tell you if it's even or odd: "))

# if number % 2 == 0:
#     print(f"\n The number {number} is even")
# else:
#     print(f"\nThe number {number} is odd")

# Intro To While Loops
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

#Letting the User choose when to quit & Using flags
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."


message = ""
while message != "quit":
    message = input(prompt)

    if message != 'quit' or message != 'QUIT':
        print(message)


# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program."

# active = True

# while active:
#     message = input(prompt)
#     # Check if user entered quit
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# Break statement
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.)"

# cities = []

# while True:
#     city = input(prompt)
#     # Test the condition to quit the loop
#     if city == 'quit':
#         break
#     else:
#         cities.append(city)
#         print(f"I'd love to go to {city.title()}!")

# List of cities entered
# print(cities)

# Using continue in a Loop
# current_num = 0
# while current_num < 10:
#     current_num += 1
#     if current_num % 2 == 0:
#         continue
    
#     print(current_num)

# Avoiding Infinite Loops
# x = 1
# while x <= 5:
#     print(x)
    # x += 1

# Using a while Loop in a a dictionary
# Start with users that need to be verified,
# and an empty list to hold confirmed users.
# uncomfired_users = ['alice', 'brian', 'candace']
# confirmed_users = []

# # Verify each user until there are no more unconfirmed users.
# # Move each verified user into the list of confirmed users
# while uncomfired_users:
#     current_user = uncomfired_users.pop()

#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)

# # Display all confirmed users
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# Removing All Instances of Specific Values from a List
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# Filling a Dictionary with User Input
reponses = {}

# set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # Prompt for person's name and reponse
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # store the responses in a dictionary
    reponses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in reponses.items():
    print(f"{name} would like to climb {response}")





    
