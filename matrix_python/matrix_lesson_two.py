def multiply(*args):
    result = 1
    for nums in args:
        result *= nums
    return result


print(multiply(2, 4, 5))
def get_info(**kwargs):
    return kwargs

