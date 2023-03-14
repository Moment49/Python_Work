# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick")
#     print(f"I can't wait to see yout next trick, {magician.upper()}")
#     print("Thank you, everyone. That was a great magic show\n") 
# # Indentation Error
# print(magician)

# Indenting Unnecessarily
# message = "Hello Python world"
#     print(message)

#Forgetting the colon
# magicians = ['alice', 'david', 'micheal']
# for magician in magicians:
#     print(magician)

# # Range() function
# for value in range(1, 6):
#     print(value)

# # Using a range() to make a list
# numbers = list(range(1, 6))
# print(numbers)

# Even_numbers
# even_numbers = list(range(2, 11, 2))
# print(even_numbers)

# # Squares
# squares = []
# for value in range(1, 11):
#     # square = value ** 2
#     squares.append(value ** 2)
# print(squares)

# Simple Statistics
# digits = []
# for digit in range(0, 10):
#    digits.append(digit)
# # A program to move the first digit to the back
# # Removing the digit from the list using the pop ()
# popped_digit = digits.pop(0)
# # print(popped_digit)
# # Appending the digit using the append method
# digits.append(popped_digit)
# print(digits) 

# print(max(digits))
# print(min(digits))
# print(sum(digits))

# List Comprehension
# squares = [value ** 2 for value in range(1, 11)]
# print(squares)

# Working with part of a List
# players = ['charles', 'martina', 'micheal', 'florence', 'eli']
# print(players[0:2])
# print(players[1:5])
# print(players[:3])
# print(players[0:4:2])
# print(players[-2:]) 
# print(players[0:4:2]) 

# Looping through a Slice
players = ['charles', 'martina', 'micheal', 'florence', 'eli']

# print("Here are the first three players on my team")
# for player in players[:3]:
#     print(player.title())

# Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_food = my_foods[:]

# print("My favourite foods are:")
# print(f"{my_foods}")
# my_foods.append('Ice Cream')
# print(my_foods)


# print("My friend's favourite foods are:")
# print(friends_food)
# friends_food.append('cannoli')
# print(friends_food)

# Tuples
# dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])

# dimensions[0] = 250

# Note tuples must be have a trailing comma (3,)
my_tuple = (3,)
print(my_tuple)

# Looping through a tuple
dimensions = (200, 50)
print("Original dimensions")
for dimension in dimensions:
    # dimension = dimension * 2
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)


















