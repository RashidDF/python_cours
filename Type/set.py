my_set1 = {10, 20, 30, 40, 50, 60}
my_set2 = {60, 70, 80, 90, 100, 110}

my_set3 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
my_set4 = {3, 4, 5, 6}

my_set5 = {'abc', 'd', 'f', 'y'}
my_set6 = {'abc', 'd', 'f', 'l'}

# Union
print('UNION')
print(my_set1.union(my_set2))
print(my_set1 | my_set2)
print('-----------------------')

# Intersection
print('Intersection')
print(my_set1.intersection(my_set2))
print(my_set1 & my_set2)
print('-----------------------')

# Difference
print('Difference')
print(my_set1.difference(my_set2))
print(my_set2.difference(my_set1))
print('-----------------------')

# Issubset
print('ISSUBSET')
print(my_set3.issubset(my_set4))
print(my_set4.issubset(my_set3))
print('-----------------------')

# Issuperset
print('Issuperset')
print(my_set3.issuperset(my_set4))
print(my_set4.issuperset(my_set3))
print('-----------------------')

# Discard
print('Discard')
print(my_set4)
print(my_set4)
print('-----------------------')

# Remove
print('Remove')
print(my_set4)
print(my_set4)
print('-----------------------')

# Copy
print('Copy')
copied_set = my_set3.copy()
print(my_set3)
print(copied_set)
print(id(my_set3) == id(copied_set))
print('-----------------------')

# Symmetric difference
print('symmetric_difference')
print(my_set5.symmetric_difference(my_set6))
print('-----------------------')
