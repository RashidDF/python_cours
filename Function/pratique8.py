from sys import getsizeof
# 1
fruits = {
    'banana': 100,
    'apple': 150,
    'lime': 50,
}

new_fruits = {k.upper(): v for k, v in fruits.items()}

print(fruits)
print(new_fruits)

# 2
my_list = ['My', 'name', 'is', 'Rashid']

new_list = [elem for elem in my_list if len(elem) > 3]

print(my_list)
print(new_list)

# 3
squares_gen = (num * num for num in range(100_000_000))
print("Generator type : ", type(squares_gen))
print("Generator size = ", getsizeof(squares_gen), 'Bait')


squares_list = [num * num for num in range(100_000_000)]
print("List type : ", type(squares_list))
print("List size = ", getsizeof(squares_list), 'Bait')
