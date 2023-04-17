# Reading an entire file
# with open("python_work/text_files/pi.txt") as file_object:
#     contents = file_object.read()
# print(contents.rstrip())

# # Reading Line by line
# # filename = 'text_files/pi.txt'
# filename = 'python_work/text_files/pi_million_digits.txt'

# # with open(filename) as file_object:
# #     for line in file_object:
# #         print(line.rstrip())

# # Making a list of lines from a file
# with open(filename) as file_obj:
#     lines = file_obj.readlines()


# pi_string = ''
# for line in lines:
#     pi_string += line.strip()

# birthday = input("Enter your birthday, in the form mmddyy: ")

# if birthday in pi_string:
#     print("Your birthday appears in the first millon digits of pi")
# else:
#     print("Your birthday does not appear in the first million digits of")

# # print(pi_string)
# print(f"{pi_string}...")
# print(len(pi_string))

# Writing multiple lines to a file
# filename = 'python_work/text_files/programming.txt'

# with open(filename, 'w') as file_obj:
#     file_obj.write("I love programming\n")
#     file_obj.write("I love creating new applications\n")

# #Appending to a file 
# with open(filename, 'a') as file_obj:
#     file_obj.write("I also love finding meaning in large datasets.\n")
#     file_obj.write("I also love creating apps that can run in a broswer.\n")

# Expections
# Handling the ZeroDivisionError Expection
# print(5/0)

# Using Try-expect Blocks
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero")


# Using Expections to Prevent Crashes
# print("Give me two numbers, and I'II divide them.")
# print("Enter 'q' to quit")

# while True:
#     first_number = input("\nFist number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
   
#     except ZeroDivisionError:
#         print(f'Cant divide {first_number} by {second_number}')

#     else:
#         print(answer)

# Handlinf fileNotFoundError

# Analyzing Text & # Failing Silently

# def count_words(filename):
#     """Count the approximate number of words in the file. """
#     try:
#         with open(filename, encoding='utf-8') as f:
#             contents = f.read()
#     except FileNotFoundError:
#         # print(f'Sorry, the file {filename} does not exist.')
#         pass
#     else: 
#         words = contents.split()
#         num_words = len(words)
#         print(f"The file {filename} has about {num_words} words.")

# filenames = ['python_work/text_files/alice.txt','python_work/text_files/moby_dick.txt',
#               'python_work/text_files/little.txt', 'python_work/text_files/genius.txt']

# for filename in filenames:
#     count_words(filename)

# Storing Data
# json.dump & json.load

import json

# numbers = [2, 3, 5, 7, 11, 13]

# filename = 'python_work/text_files/numbers.json'
# with open(filename, 'w') as f:
#     json.dump(numbers, f)

# Json.load()
# filename = 'python_work/text_files/numbers.json'
# with open(filename) as f:
#     numbers = json.load(f)

# print(numbers)

# Saving and Reading User Generated data
# username = input("What is your name? ")

# filename = 'python_work/text_files/numbers.json'
# with open(filename, 'w') as f:
#     json.dump(username, f)
#     print(f"We'll remember you when you come back, {username}!")

# # #Greet User
# with open(filename) as f:
#     username = json.load(f)
#     print(f"Welcome back, {username}!")

# Combining the programs
import json

def get_stored_username():
    """Get stored username if avaliable"""
    filename = 'python_work/text_files/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
       return None
    else:
        return username

def get_new_username():
    """Prompt for new username"""
    filename = 'python_work/text_files/username.json'
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name"""
    correct_username = input("Please enter your correct username: ")
    username = get_stored_username()
    if username:
        if correct_username == username:
            print(f"Welcome back, {username}")
        else:
            print(f"{correct_username} does not match with the username stored {username}")
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}")

greet_user()