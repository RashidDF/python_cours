# try:
#     print(10 / 0)
# except ZeroDivisionError as e:
#     # print("Error - Division by zero!")
#     print(isinstance(e, Exception))
#     print(e)
# except TypeError as e:
#     print('Error : ' + str(e))
# else:
#     print("There was no error")
# finally:
#     print('Continue...')

# ***************************************


def divide_nums(a, b):
    if (b == 0):
        raise ValueError("Second argument can't be 0")
    return a / b


try:
    divide_nums(10, 0)
except ZeroDivisionError as ex:
    print(f"Error: {ex}")
except ValueError as ex:
    print(ex)
finally:
    print('Continue ...')
