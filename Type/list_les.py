# 1
my_list = [10, 10.5, "This is list", True, 'd']
print(my_list)

ele_sup = my_list.pop(2)
print("Element supprimer : " + ele_sup)
print(my_list)

print(len(my_list))

my_list.reverse()
print(my_list)

other_list = ['xyz', 123]
print(other_list)

my_list.extend(other_list)
print(my_list)

# 2
first_list = [1, 2, 3]
seconde_list = [4, 5, 6]

print(first_list)
print(seconde_list)

common_list = first_list + seconde_list
print(common_list)

other_common_list = first_list.__add__(seconde_list)
print(other_common_list)
