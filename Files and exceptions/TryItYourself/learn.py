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
filename = "python_work/text_files/users.txt"
           
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
file_name = "python_work/text_files/poll.txt"

prompt =  "\n(Enter quit or 'q' to abort program any)"
prompt += "\nEnter your username: "



poll_active = True

while poll_active:
    # print('keep')
    username = input(prompt)
    if username == 'q': 
        message = "Program aborted"
        print(message)
        break
    user_response = input('Enter your reason for loving programming and I will save it for you: ')
    if user_response == 'q':
        poll_active = False
        message = "Program aborted"
        print(message)
        
    else:
       with open(file_name, 'a') as file_obj:
           file_obj.write(f"\n{username}"+ ":" + f"{user_response}")



       

