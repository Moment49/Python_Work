# 5.1
motors_list = ['Subaru', 'chevrolet', 'G-wagon', 'Toyota']
new_motor = 'BMW'

# if 'subaru' in motors_list:
#     print("Is 'subaru' in motors_list? I predicted True")
#     print('subaru' in motors_list)

#     print("\nIs 'honda' in motors_list? I predicted false")
#     print('honda' in motors_list)


# 5.2
age = 13
age_2 = 25

# if age >= 18:
#     print("Is 'age' > 18? I predicted True")
#     print(age >= 18)
# if age_2 == 45:
#     print('I predicted true')
# if age == 18 or age_2 >= 21:
#     print("You are an adult youth") 
# if age >= 12 and age_2 <= 25:
#     print('You are an adolence')

# name = 'Elvis'
# if name == "Elvis":
#     print("I predicted True")
#     print(name == 'Elvis')
# if name != 'Frank':
#     print('I predicted False')
#     print(name != 'Frank')

# # Lower method
# for motor in motors_list:
#     if motor.lower() == 'subaru':
#         print('\n',True)

# Not in a list (False condition)
if new_motor not in motors_list:
    print(True)
    print(new_motor not in motors_list)