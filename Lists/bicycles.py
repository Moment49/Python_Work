# # bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# # print(bicycles)

# # # Acessing Elements in a list
# # print(bicycles[0].title())
# # print(bicycles[-1])
# # # Using Individual Values from a List
# # message = f"My first bicycle was a {bicycles[0].upper()}"
# # print(message)
# # # Changing Adding and Removing Elements
# # motorcycles = ['honda', 'yamaha', 'suzuki']
# # print(motorcycles)
# # motorcycles[0] = 'ducati'
# # print(motorcycles)
 
# #Appending Elements to a List
# motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles.append('ducati')
# print(motorcycles)
# # Removing Elements from a List
# motorcycles = ['honda', 'yamaha', 'suzuki']
# del motorcycles[1]
# print(motorcycles)

# # Pop() method
# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# last_owned = motorcycles.pop(0)
# print(f"The last motorcycle I owned was a {last_owned.title()}.")
# # Removing an Item by value
# motorcycles.remove('yamaha')
# print(motorcycles)

# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print(f"\nA {too_expensive} is too expensive for me")

# Sort() method
# cars = ['bmw', 'audi', 'toyota', 'sabaru']
# # cars.sort() 
# print("Here is the original list")
# print(cars)

# print("\nHere is the sorted list: ")
# print(sorted(cars))

# print("\nHere is the original list again")
# print(cars)

# Reverse order
# cars.sort(reverse=True)
# print(cars)

# reserve() method
# cars.reverse()
# print(cars)

# Length of a list len()
cars = ['bmw', 'audi', 'toyota', 'sabaru']
# len(cars)
print(len(cars))

# Avoiding Index Errors When Working with Lists
print(cars[5]) 

