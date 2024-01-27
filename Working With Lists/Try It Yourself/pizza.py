# # 4.1 Pizzas
pizzas = ['pepperoni', 'cheese', 'kimchi', 'salmon', 'Peking', 'Tom']
# For loop
for pizza in pizzas:
    # print(pizza)
    print(f"I like {pizza} pizza")
print(f"I love pepperoni, cheese and kimchi pizaa because the are the best\n"
    "The pizza the sell in domino is one of the best in the world")
print("I really love pizza!")        

# 4.2 Animals
# animals = ['Horse', 'Cat', 'Dog']

# # Use a for loop to print each animal name
# for animal in animals:
#     # print(animal)
#     print(f"A {animal.upper()} will make a great pet")

# print("Any of these animals would make a great pet")

# 4. Counting to twenty
# for count in range(1, 21):
#     print(count)

# # 4.4 One million
# millions = list(range(1, 1_000_001))
# # print(millions) 
# for million in millions:
#     print(million)

#4.5 Sum a million
# numbers = list(range(1, 1_000_001))
# min_value = min(numbers)
# print(f"{min_value}\n")
# max_value = max(numbers)
# print(f"{max_value}\n")
# sum_value = sum(numbers)
# print(f"{sum_value} \n")

# # 4.6 Odd Numbers
# odd_numbers = []
# for value in range(1, 21, 3):
#     odd_numbers.append(value)
#     print(f"Odd No:{value}\n")
# print(odd_numbers)

# 4.7 Threes
# Using a list comprehension
# multiples = [value ** 3 for value in range(3, 31)]
# print(multiples)

# multiples_list = []
# for value in range(3, 30):
#     multiple = value ** 3
#     multiples_list.append(multiple)
#     print(f"These are the numbers: {multiple}")
# print(multiples_list)

#4.8
# cubes = []
# for cube in range(1, 11):
#     cube_no = cube ** 3
#     cubes.append(cube_no)
# print(cubes)

# # 4.9 Cube List comprenhension
# cubes = [cube ** 3 for cube in range(1, 11)]
# print(cubes)
# odd_no = [ value for value in range(1, 11) if value % 2 != 0]
# print(odd_no)

# 4.10
foods = ['pizza', 'falafel', 'carrot cake', 'beans', 'yam', 'sauce', 'egusi']
# print("The first three items in the list are:") 
# for food in foods[:3]:
#     print(food) 

# print("Three items from the middle of the list are:")
# for food in foods[2:-2]:
#     print(food)   

# print("The last three items in the list are:")
# for food in foods[-3:]:
#     print(food)    

# 4.11My Pizza, Your Pizza
# pizzas = ['pepperoni', 'cheese', 'kimchi', 'salmon', 'Peking', 'Tom']
# friends_pizza = pizzas[:]
# print(friends_pizza)

# pizzas.append('macroni')
# print(pizzas)

# friends_pizza.append('chilli')
# print(friends_pizza)

# # Using a for loop to print the lists
# print(f"My favourite pizza are:")
# for pizza in pizzas:
#     print(pizza)

# print(f"My friend's favourite pizza are:")
# for friend_pizza in friends_pizza:
#     print(friend_pizza)


# 4.12 More Loops
# foods = ['pizza', 'falafel', 'carrot cake', 'beans', 'yam', 'sauce', 'egusi']

# print("List of food Items from the list: ")
# for food_item in foods:
#     print(food_item)

# 4.13
# foods = ('Sauce', 'Fried rice', 'jollof rice', 'Macaroni', 'Eba')
# for food in foods:
#     print(food)

# Modifying the tuple
# foods[3] = 'Salad'
# print(foods)

# foods = ('Sauce', 'Fried rice', 'jollof rice', 'Ice cream', 'salad')
# for food in foods:
#     print(food)