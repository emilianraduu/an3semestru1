def showsXTimes(x, *list):
    apperences = []
    for item in list:
        for value in item:
                apperences.append(value)

    result = []

    for item in apperences:
        if apperences.count(item) == x and item not in result:
            result.append(item)
    return result

print(showsXTimes(3, [1, 2, "test"], [5, 2, 3], [5, 2, "test"]))
