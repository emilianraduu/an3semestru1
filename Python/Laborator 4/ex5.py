globalDictionary = {
    "+": lambda *a, **k: print(a, k),
    "-": lambda *a, **k: print(a, k, sep=", "),
    "/": lambda *a, **k: print(a),
    "%": lambda *a, **k: print(k)
}

globalDictionary2 = {"+": lambda a, b: a + b, "*": lambda a,
                     b: a * b, "/": lambda a, b: a / b, "%": lambda a, b: a % b}

globalDictionary3 = {"+": lambda a, b: a - b, "*": lambda a,
                     b: a // b, "/": lambda a, b: a ** b, "%": lambda a, b: a - b}


def dictionaries(*dict):
    newDict = {}
    for item in dict:
        for object in item:
            if object in newDict:
                if not isinstance(newDict[object], list):
                    newDict[object] = [newDict[object]]
                newDict[object].append(item.get(object))
            else:
                newDict[object] = item.get(object)
    print(newDict)
    return newDict


dictionaries(globalDictionary, globalDictionary2, globalDictionary3)
