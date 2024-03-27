set_int_one = {10, 25, 36, 78, 15}
set_int_two = {5, 10, 22, 36, 45, 17}

set_int_one.add(17)
print(set_int_one)
print(set_int_two)

set_int_union = (set_int_one | set_int_two)
print('Union : ' + str(set_int_union))

set_int_diff = (set_int_one.difference(set_int_two))
print('Difference : ' + str(set_int_diff))

set_int_inters = (set_int_one & set_int_two)
print('Intersection : ' + str(set_int_inters))

list_int_union = list(set_int_union)
print(list_int_union)
