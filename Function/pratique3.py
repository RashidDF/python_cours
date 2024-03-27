set_one = {10, 25, 36, 78, 15}
set_two = {10, 25, 36, 78, 15}

print(set_one == set_two)
print(set_two.__eq__(set_one))

print(set_one is set_two)

print(10 in set_one)

print(100 in set_two)
