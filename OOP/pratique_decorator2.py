def log_function_call(fn):
    def wrapper(*args, **kwargs):
        print(f"Function name: {fn.__name__}")
        print(f"Function arguments: {args}, {kwargs}")
        result = fn(*args, **kwargs)
        print(f"function result: {result}")
        return result
    return wrapper


@log_function_call
def mult(a, b):
    return a * b


mult(5, 2)


print("************************")


@log_function_call
def sum(a, b):
    return a + b


sum(a=40.3, b=20.7)
