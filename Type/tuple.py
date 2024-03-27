exist_tuple = (1, 2, 3, 4, 5)
new_tuple = (6, 7, 8, 9, 10)

# print(exist_tuple.count(5))

my_list = list(exist_tuple)
print(type(my_list))
print(my_list)

my_list.append(6)
print(my_list)

exist_tuple = tuple(my_list)
print(type(exist_tuple))
print(exist_tuple)


# print(exist_tuple)
# print(new_tuple)

# exist_tuple += new_tuple

# print(exist_tuple)
