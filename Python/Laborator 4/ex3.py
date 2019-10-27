def apply_operator(operator, a, b):
    for item in globalDictionary:
        if operator==item:
            return globalDictionary.get(item)(a,b)


globalDictionary = {"+": lambda a, b: a + b, "*": lambda a,
                    b: a * b, "/": lambda a, b: a / b, "%": lambda a, b: a % b}


print(apply_operator('%', 1, 2))