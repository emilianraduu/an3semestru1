import re

def read():
    file = open('labirinths.txt', 'r')
    lines = list(file.readlines())
    labirint = []
    for i in lines:
        i = re.sub('[\s+]', '', i)
        numbers = [ int(x) for x in i]
        labirint.append(numbers)
    return labirint