from math import sqrt
import itertools


def fibo(n):
    if(n == 1):
        return n
    elif n == 2:
        return n
    elif n ==3:
        return n
    else:
        return (int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))))


def is_prime(number):
    if(number == 1):
        return False
    elif (number == 2):
        return True
    else:
        for i in range(2, int(number/2)+1):
            if (number % i) == 0:
                return False
    return True


def custom_filter(my_list):
    new_list = []
    for item in my_list:
        if(is_prime(item) and item == fibo(item)):
            new_list.append(item)
    return sorted(new_list)


def get_number_from_text(text):
    number = ''
    for i in range(0, len(text)):
        try:
            k = int(text[i])
            number += text[i]
        except:
            return number

    return number


def extract_numbers(text):
    numbers = []
    i = 0
    while (i < len(text)):
        try:
            k = int(text[i])
            x = get_number_from_text(text[i:])
            numbers.append(int(x))
            i += len(x)
        except:
            i += 1
    return sorted(numbers, reverse=True)


def special_sum(*params):
    numbers = []
    for item in params:
        k = -1
        for number in extract_numbers(item):
            if(number % 2 == 0 and number > k):
                k = number
        numbers.append(k)
    return sum(numbers)


