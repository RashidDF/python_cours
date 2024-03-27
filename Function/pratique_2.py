def merge_lists_to_dict(list1, list2):
    if (len(list1) != len(list2)):
        print('Error! list1.size not equal list2.size')
        return
    return dict(zip(list1, list2))


fruits = ['apple', 'banana', 'lime']
quantities = [100, 70, 50]

print(merge_lists_to_dict(list1=fruits, list2=quantities))


def update_car_info(**car):
    car['is_available'] = True
    return car


car_info = update_car_info(brand='BMW', price=100000)
print(car_info)
