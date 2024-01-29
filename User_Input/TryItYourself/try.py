# # 7.1 RentaL Car
# # car_type = input("What kind of rental care do you like? ")
# # print(f"\nLet me see if I can find you a {car_type}")

# # 7.2 Restaurant Seating
# # people_num = input("How many people are in this dinner group? ")
# # people_num = int(people_num)

# # if people_num > 8:
# #     print("You guys will have to wait for a table")
# # else:
# #     print("Your table is ready")

# # 7.3 Multiples of Ten
# # num = int(input("Enter a number andI will tell you if its a multiple of 10: "))

# # if num % 10 == 0:
# #     print(f"{num} is a multiple of 10")
# # else:
# #     print(f"{num} is not a multiple of 10")

# # 7.4 Pizza Toppings
# prompt = "\nPlease enter your favorite pizza topping"
# prompt += "\nEnter 'quit' to end program: "

# # Set an active flag
# # isMakePizza = True
# # while isMakePizza:
# #     # Accept user input
# #     topping = input(prompt)
    
# #     # Test for condition to end the program
# #     if topping == 'quit' or topping == 'q':
# #         break
# #     else:
# #         print(f"I'II add the {topping} topping to your pizza")

# # 7.5 Movie Tickets
# # prompt = "Enter your age and I'II tell you the cost of movie ticket: "

# # while True:
# #     # Get the user Input
# #     age = int(input(prompt))

# #     # Conditional Tests
# #     if age < 3:
# #         print("Viola!!! The movie ticket is free")
# #     elif age >= 3 and age <= 12:
# #         price = 10
# #         print(f"The movie ticket cost is ${price}")
# #     else:
# #         price = 15
# #         print(f"The movie ticket cost is ${price}")

# # 7.6 Three Exits
# # isMakePizza = True
# # while isMakePizza:
# #     # Accept user input
# #     topping = input(prompt)
# #     # Test for condition to end the program
# #     if topping == 'quit' or topping == 'q':
# #         break
# #     else:
# #         print(f"I'II add the {topping} topping to your pizza")

# # 7.7 Inifinity
# # letter = "Elvis"
# # while letter:
# #     print(letter)

# # counter = 0
# # while counter < 5:
# #     print(counter)

# # 7.8 Deli
# # sandwich_orders = ['pastrami', 'bacon', 'pastrami', 'macroni', 'pastrami','spagellti']
# # finished_sandwichs = []

# # while sandwich_orders:
# #     # Get your sandwich
# #     sandwich = sandwich_orders.pop()
# #     print(f"\nI making your {sandwich} sandwich")

# #     # Append to the finished sandwich list
# #     finished_sandwichs.append(sandwich)
# # #List of all the sandwich made
# # print("\nThis is a list of all the sandwich a made for you:")
# # for finised_sandwich in finished_sandwichs:
# #     print(f"I made you a {finised_sandwich} sandwich")

# # 7.9
# # sandwich_orders = ['pastrami', 'bacon', 'pastrami', 'macroni', 'pastrami','spagellti']
# # finished_sandwichs = []
# # print("I'm sorry deli we have run out of pastrami")

# # while 'pastrami' in sandwich_orders:
# #     sandwich_orders.remove('pastrami')

# # print("\n")
# # while sandwich_orders:
# #     # Get your sandwich
# #     sandwich = sandwich_orders.pop()
# #     print(f"I am making your {sandwich} sandwich")

# #     # Append to the finished sandwich list
# #     finished_sandwichs.append(sandwich)
# # #List of all the sandwich made
# # print("\nThis is a list of all the sandwich a made for you:")
# # for finised_sandwich in finished_sandwichs:
# #     print(f"I made you a {finised_sandwich} sandwich")

# # 7.10 Dream Vacation
# # Poll responses
# responses = {}

# poll_active = True
# while poll_active:
#     name = input("\nWhat is your name? ")
#     reponse = input("\nIf you could visit one place in the world, where would you go?")

#     # Store the response in the dictionary
#     responses[name] = reponse

#     #Ask the user if he/she wants to quit
#     repeat = input("Would you like to let another person respond? (yes/ no) ")
#     if repeat == 'no':
#         poll_active = False

# # Polling is complete. Show the results.
# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(f"{name} would like to visit {response}")



