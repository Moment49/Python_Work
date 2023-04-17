# 10.1 Learning python
# filename = "python_work/text_files/learn.txt"

# with open(filename) as file_obj:
#     open_contents = file_obj.read()
#     print(open_contents)

# with open(filename) as file_obj:
#     open_contents = file_obj.readlines()

# contents = []
# for content in open_contents:
#     contents.append(content.rstrip())
#     print(f'{content.rstrip()}')

# print(contents)
# print()

# with open(filename) as file_obj:
#     for line in file_obj:
#         print(line.rstrip())

# 10.2
# with open(filename) as obj_file:
#     for line in obj_file:
#         print(line.replace('python', 'C').rstrip())

# 10.3
# filename = "python_work/text_files/users.txt"

# Ask for user Input
# username = input("Please enter your name and I will save it for you: ")

# # Write the usernames to the file object and save
# with open(filename, 'w') as file_obj:
#     file_obj.write(username)

# 10.4 Guest Book
# filename = "python_work/text_files/users.txt"
           
# prompt =  "\nEnter quit or 'q' to exit"
# prompt += "\nEnter a username and I will save it for you: "

# while True:
#     # Get User Input
#     username = input(prompt)
#     # Condition to abort program
#     if username == 'quit' or username == 'q':
#         message = "Program aborted"
#         print(message)
#         break  
#     else:
#         message = f'welcome  {username}'
#         print(message)
#           # Write to the file and save username 
#         with open(filename, 'a') as file_obj:
#             file_obj.write(f"\n{username.rstrip()}")
     
# Refactoring 
# A function to Get userInput
# def getUserName():
#     """Get username from Input"""
#     prompt =  "\nEnter quit or 'q' to exit"
#     prompt += "\nEnter a username and I will save it for you: "
#     username = input(prompt)
#     return username

# # A function to write userInputs to a file
# def writeUsername(filename):
#     with open(filename, 'a') as file_obj:
#         file_obj.write(f"\n{user}")


# A program to ask for UserInput and store it in a file
# while True:
#     user = getUserName()
#     if user == 'quit' or user == 'q':
#         message = "Program aborted"
#         print(message)
#         break  
#     else:
#         message = f'welcome  {user}'
#         print(message)
#         # Write to the file and save username 
#         writeUsername(filename)

# 10.5
# file_name = "python_work/text_files/poll.txt"

# prompt =  "\n(Enter quit or 'q' to abort program any)"
# prompt += "\nEnter your username: "



# poll_active = True

# while poll_active:
#     # print('keep')
#     username = input(prompt)
#     if username == 'q': 
#         message = "Program aborted"
#         print(message)
#         break
#     user_response = input('Enter your reason for loving programming and I will save it for you: ')
#     if user_response == 'q':
#         poll_active = False
#         message = "Program aborted"
#         print(message)
        
#     else:
#        with open(file_name, 'a') as file_obj:
#            file_obj.write(f"\n{username}"+ ":" + f"{user_response}")

# 10.6 & 10.7
# while True:
#     try:
#         first_num = int(input("First number: "))
#         second_num = int(input("second number: "))
#         anwser = first_num + second_num
#     except ValueError:
#         print("Please enter a number")
#     else:
#         print(anwser)
#         break

# 10.8 & 10.9
# filenames = ["python_work/text_files/cats.txt", "python_work/text_files/dogs.txt", "python_work/text_files/chicks.txt"]

# for filename in filenames:
#     try:
#         with open(filename, encoding='utf-8') as f:
#             contents = f.read()   
#     except FileNotFoundError:
#         pass
#         # print(f"Sorry, the filename {filename} does not exist.")
#     else:
#         print(f"\nThe filename {filename} contents: \n{contents}")

# 10.10 Common words
# file_name = "python_work/text_files/counts.txt"

# with open(file_name, encoding='utf-8') as f:
#     contents = f.read()
#     print(f"The word 'the' appears {contents.rstrip().lower().count('the ')} in the filename {file_name}")
    

# 10.11
import json

#Json.load() 
def get_stored_num():
    """Get stored user number if avaliable"""
    filename = 'python_work/text_files/fav_numbers.txt'
    try:
        with open(filename) as f:
            user_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return user_number

def get_new_number():
    """"Get user number if its not stored"""
    filename = 'python_work/text_files/fav_numbers.txt'
    user_number = input('Enter your favorite number: ')
    with open(filename, 'w') as f:
        json.dump(user_number, f)
    return user_number
           

def show_user_number():
    """"Show user number if avaliable"""
    user_number = get_stored_num()
    if user_number:
         print(f"I know your favorite number! It's {user_number}")
    else:
        user_number = get_new_number()
        print(f'I will save {user_number} as your favorite number')


get_new_number()
show_user_number()
