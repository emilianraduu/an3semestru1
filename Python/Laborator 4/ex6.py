givenDict = {
    'a': 1,
    'b':
    {
        'c': 3,
        'd':
        {
            'e': 5,
            'f': 6
        }
    }
}


def getNestedValues(dictionary):
    list = []
    for key, value in dictionary.items():
        if isinstance(value, dict):
            # print(key, getNestedValues(value))
            list.append((key))
            getNestedValues(value)
        else:
            list.append((key, value))
    print(list)


getNestedValues(givenDict)