# https://softuni.bg/trainings/resources/video/84083/
# video-22-may-2023-ines-kenova-python-advanced-may-2023/4106
# args
# with *args we pack arguments as a tuples. args is variable. The important is "*".
# It is not necessary to be "args" but is good practice to stay.
def sum_nums(*args):
    result = 0
    for num in args:
        result += num
    return result


# when function is called, the number of arguments is not defined
print(sum_nums(23, 15, 48, 32))

# kwargs
# when we want to pack arguments as a dictionaries using "**" and "kwargs"
# as in args, kwargs is not mandatory name of this variable but is good practice
# the mandatory are only "**" and variable after that


def my_dict(**kwargs):
    # here we tread kwargs as a dictionary using methods for it
    for key, values in kwargs.items():
        print(f"The key is {key}, the values are {values}")


my_dict(a=(6, 3), b=7, c=True)


# args and kwargs can be used together
def both(*args, **kwargs):
    print(args)
    for key, values in kwargs.items():
        print(f"The key is {key}, the values are {values}")


# In args going not named arguments, in kwargs named
both(5, 6, 7, w=(7, 5), y="harsp", p=False)

=======================
ef fill_the_box(*args):
    box = args[0] * args[1] * args[2]
    small_boxes = []
    for s in args[3:]:
        if s == "Finish":
            break
        else:
            small_boxes.append(s)

    if sum(small_boxes) <= box:
        return f"There is free space in the box. You could put {box - small_boxes} more cubes."
    else:
        return f"No more free space! You have {small_boxes - box} more cubes."