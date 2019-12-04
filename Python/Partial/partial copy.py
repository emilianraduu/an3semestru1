def problema1(n):
    bin_n = bin(n)
    count = 0
    # print(len(bin(n)))
    for i in bin_n:
        if i == '1':
            count += 1
    return count


def patrat_perfect(n):
    for i in range(0, n):
        if i * i == n:
            return True
    return False


def problema2(n):
    for i in range(n, 0, -1):
        if patrat_perfect(i):
            return i


def biggest_palindrom(list):
    max = int(list[0])
    for i in list:
        if int(i) > max:
            max = int(i)
    return int(max)


def get_palindroms(list):
    new_list = []
    for i in list:
        y = str(i)
        if y == y[::-1]:
            new_list.append(y)
    return new_list


def problema3(my_list):
    my_list = get_palindroms(my_list)
    return (len(my_list), biggest_palindrom(my_list))


def get_next_fazan(my_list, last_letters):
    for i in my_list:
        if i[:2] == last_letters:
            return i


def problema4(my_list, letter):
    for i in my_list:
        if i[0] == letter:
            first_word = i
    my_list.remove(first_word)
    new_list = []
    new_list.append(first_word)
    prev_word = first_word
    while(my_list):
        last_letters = prev_word[-2:]
        next_word = get_next_fazan(my_list, last_letters)
        my_list.remove(next_word)
        new_list.append(next_word)
        prev_word = next_word
    return new_list

def problema5(matrix):
    cant_see = []
    row_len = len(matrix[0])
    for i in range(0,row_len):
        for item in matrix:
            print(item[i])
        print('\n')
