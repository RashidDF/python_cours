my_dict = {}

for i in range(3):
    dict_key = input("\nInsert key number "+str(i+1)+" for dictionary: ")
    dict_value = input("\nInsert value for key "+dict_key+" for dictionary: ")

    # my_dict[dict_key] = dict_value
    my_dict.update({dict_key: dict_value})


print(my_dict)

my_dict['price'] = 20000

print(my_dict)

del my_dict['price']

print(my_dict)
