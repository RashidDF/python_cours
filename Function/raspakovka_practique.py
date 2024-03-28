my_list_car = [
    {'brand': 'Toyota', 'model': 'RAV4', },
    {'brand': 'Mercedes', 'model': 'S600', },
    {'brand': 'BMW', 'model': 'X5', }
]


def info_car(brand, model):
    return f"Brand: {brand}, model: {model}"


toyota, mercedes, bmw = my_list_car
print(toyota)
print(mercedes)
print(bmw)

print(info_car(**toyota))
print(info_car(**mercedes))
print(info_car(**bmw))
