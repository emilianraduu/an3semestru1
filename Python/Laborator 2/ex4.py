

def intersection(a, b):
    result = []
    for i in a:
        for j in b:
            if i == j:
                result.append(i)
    return sorted(result)


def reunion(a, b):
    result = []
    for i in a:
        result.append(i)
    for j in b:
        if j not in result:
            result.append(j)
    return sorted(result)


def difference(a, b):
    result = []
    for i in a:
        result.append(i)
    for j in b:
        if j in result:
            result.remove(j)
    return sorted(result)

# def operation(a, b):
#     return (a intersectat cu b, a reunit cu b, a - b, b - a)


a = [1, 3, 5, 7]
b = [2, 8, 12, 5, 9]
print(difference(b, a))
