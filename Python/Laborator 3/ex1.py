def myFunc(a, b):
    return ([value for value in a if value in b], 
    list(set(a) | set(b)), 
    [value for value in a if value not in b], 
    [value for value in b if value not in a])


a = [1, 2, 3, 8, 9]
b = [4, 5, 6, 3, 1, 2]
print(myFunc(a, b))
