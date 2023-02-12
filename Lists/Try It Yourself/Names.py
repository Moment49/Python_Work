# # # # 3.1 Names
# # # names = ['Elvis', 'Gift', 'Jane', 'Kelvin', 'Favour']
# # # # print(names[0])
# # # # print(names[1])
# # # # print(names[2])
# # # # print(names[3])
# # # # print(names[-1])

# # # # 3.2 Greetings
# # # message = "This is going to be an awesome python programming journey"
# # # print(f"{message} {names[0]}")
# # # print(f"{message} {names[1]}")
# # # print(f"{message} {names[2]}")
# # # print(f"{message} {names[3]}")
# # # print(f"{message} {names[-1]}")

# # # # 3.3 Your Own List
# # # cars = ['bmw', 'audi', 'mercedes', 'porche', 'benz']

# # # print( f"I would like to own a {cars[0]} car")
# # # print( f"I would like to own a {cars[1]} car")
# # # print( f"I would like to own a {cars[2]} car")
# # # print( f"I would like to own a {cars[3]} car")
# # # print( f"I would like to own a {cars[-1]} car")

# # # 3.4 Guest List
# # guest_list = ['Ade', 'Ada', 'Mom']
# # # print(f'{guest_list[0]} You are invited for dinner at my place')
# # # print(f'{guest_list[1]} You are invited for dinner at my place')
# # # print(f'{guest_list[-1]} You are invited for dinner at my place')
# # # # 3.5
# # unavailable_guest = 'Ada'
# # guest_list.remove(unavailable_guest)
# # # print(f"The name of the guest that cant come to the dinner is {unavailable_guest}")

# # guest_list = ['Ade', 'Ada', 'Mom']
# # guest_list[1] = 'Nkechi'
# # print(guest_list)

# # print(f'{guest_list[0]} You are invited for dinner at my place')
# # print(f'{guest_list[1]} You are invited for dinner at my place')
# # print(f'{guest_list[-1]} You are invited for dinner at my place')

# # 3.6
# # print(f"Hello {guest_list[0]}, {guest_list[1]} and {guest_list[-1]} more guest are going to join us")
# # Adding guests to the list
# # guest_list.insert(0, 'Nneka')
# # guest_list.insert(2, 'David')
# # guest_list.append('Kelvin')
# # print(f'{guest_list[0]} You are invited for dinner at my place')
# # print(f'{guest_list[1]} You are invited for dinner at my place')
# # print(f'{guest_list[2]} You are invited for dinner at my place')
# # print(f'{guest_list[3]} You are invited for dinner at my place')
# # print(f'{guest_list[4]} You are invited for dinner at my place')
# # print(f'{guest_list[-1]} You are invited for dinner at my place')

# # 3.7
# countries = ['Rome', 'Canada', 'Berlin', 'Moscow', 'Usa']
# # print("\nThis is the original list")
# # print(countries)
# # print("\nThis is the Sorted List")
# # print(sorted(countries))

# # print("\nThis the orginal list again")
# # print(countries)

# # Using the sorted() to reverse a list
# print(sorted(countries))
# print(sorted(countries, reverse=True))

# Using reversed()
# countries.reverse()
# print(countries)
# countries.reverse()
# print(countries)

# # Using the Sort()
# countries.sort()
# print(countries)
# countries.sort(reverse=True)
# print(countries)

# 3.9 Dinner Guests
guest_list = ['Ade', 'Ada', 'Mom']
print(f"I am inviting {len(guest_list)} Guests to the dinne party")

# 3.10 Every Function
languages = []
languages.append('French')
languages.append('English')
languages.append('Dutch')
languages.append('German')
languages.append('Latin')
print(languages)
languages[0] = "Normadaic"
print(languages)
# Pop()
popped_lang = languages.pop(0)
print(popped_lang)
# Insert
languages.insert(0, 'Greek')
print(languages)


absolete_lang = 'Latin'
languages.remove(absolete_lang)
print(absolete_lang)
print(languages)

del languages[0]
print(languages)

languages.sort()
print(languages)
print(sorted(languages))
languages.reverse()
print(languages)