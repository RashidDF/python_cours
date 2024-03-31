# 1
print("Tache : 1")


def dict_to_list(my_dict):
    result_list = []
    for k, v in my_dict.items():
        k = double_int(k)
        result_list.append({k, v})
    return result_list


def double_int(any_value):
    if type(any_value) is int:
        return any_value * 2
    return any_value


my_dict = {
    5: 'five_int',
    '5': 'five_str',
}
print(my_dict)
print(dict_to_list(my_dict))

# 2
print("\nTache : 2")


def filter_list(any_list, filter_type):
    result_list = []
    for value in any_list:
        if (type(value) is filter_type):
            result_list.append(value)
    return result_list


print(filter_list([35, True, 'abc', 10], int))
print(filter_list([35, True, 'abc', 10], str))
print(filter_list([35, True, 'abc', 10], bool))

# 3
print("\nTache : 3")


def filter_list2(list_to_filter, value_type):
    return list(filter(lambda elem: type(elem) is value_type, list_to_filter))


print(filter_list2([35, True, 'abc', 10], int))
print(filter_list2([35, True, 'abc', 10], str))
print(filter_list2([35, True, 'abc', 10], bool))
