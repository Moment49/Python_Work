# Reading an entire file
# with open("python_work/text_files/pi.txt") as file_object:
#     contents = file_object.read()
# print(contents.rstrip())

# # Reading Line by line
# # filename = 'text_files/pi.txt'
filename = 'python_work/text_files/pi_million_digits.txt'

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
filename = 'python_work/text_files/programming.txt'

# with open(filename, 'w') as file_obj:
#     file_obj.write("I love programming\n")
#     file_obj.write("I love creating new applications\n")

# #Appending to a file 
# with open(filename, 'a') as file_obj:
#     file_obj.write("I also love finding meaning in large datasets.\n")
#     file_obj.write("I also love creating apps that can run in a broswer.\n")

# Expections