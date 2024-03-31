def route_info(info):
    if ('distance' in info) and info['distance'] > 0:
        return (f"Distance to your destination is {info['distance']}")

    if (('speed' in info and 'time' in info)
            and (info['speed'] > 0 and info['time'] > 0)):
        return (f"Distance to your destination is {info['speed'] * info['time']}")

    return ("No distance info is available")


info1 = {'distance': 100, 'speed': 50, 'time': 2, }
info2 = {'distance': 0, 'speed': 75, 'time': 2, }
info3 = {'speed': 110, 'time': 2, }
info4 = {'speed': 0, 'time': 3, }
info5 = {'speed': 200, 'time': -1, }
info6 = {}

print('info1 : ', route_info(info1))
print('info2 : ', route_info(info2))
print('info3 : ', route_info(info3))
print('info4 : ', route_info(info4))
print('info5 : ', route_info(info5))
print('info6 : ', route_info(info6))
