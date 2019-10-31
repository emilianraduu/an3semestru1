def problem1(my_list):
    index_of_even = []
    index_of_odd = []
    for index, item in enumerate(my_list):
        if int(item % 2) == 0:
            index_of_even += 1
        if int(item % 2) == 1:
            index_of_odd += 1
        


problem1([1, 3, 5, 2, 8, 7, 4, 10, 9, 2])


def problem2(pairs):
    result = []
    for item in pairs:
        result_for_item = {
            'sum': item[0]+item[1],
            'prod': item[0]*item[1],
            'pow': item[0]**item[1]
        }
        result.append(result_for_item)
    return result
