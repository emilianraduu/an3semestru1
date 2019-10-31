def my_function(*args, **kwargs):
    sum = 0
    for i in range(0, len(args)):
        sum += args[i]
    for i in range(0, len(kwargs)):
        sum += list(kwargs.values())[i]
    return sum


my_function(1, 2, c=3, d=4)
