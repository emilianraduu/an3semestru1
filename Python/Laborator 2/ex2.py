def isPrime(nr):
    for i in range(2,int(nr/2)+1):
        if (nr%i)==0:
            return False
    return True

def getPrimes(list):
    primes = []
    for i in list:
        if isPrime(i):
            primes.append(i)
    return primes

list = [2,3,4,5,6,25,112,17]
print (getPrimes(list))