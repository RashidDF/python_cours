import json

my_dict = {
    'Number': 2,
    'String': 'qwerty',
    'Boolean': True,
    'List': [10, 10.5, "This is list", True, 'd'],
    'tuple': (1, 2, 3, 4, 5),
    'dict': {
        'a': 1,
        'b': 2,
        'c': 3,
    }
}

my_json = json.dumps(my_dict, indent=4)

print(my_json + "\n\n")
print(type(my_json))
