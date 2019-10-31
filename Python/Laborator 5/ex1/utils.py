import sys


def process_item(x):
    def isPrime(item):
        for i in range(2, int(item**1/2)+1):
            if item % i == 0:
                return False
        return True
    for item in range(x, sys.maxsize**10):
        if isPrime(item) == True:
            return item


if __name__ == '__main__':
    try:
        x = int(input('Insert a number : '))
        process_item(x)
    except:
        print('[ERROR] Insert a valid number')
else:
    print('[UTILS MODULE LOADED]')
