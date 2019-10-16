def nFibo(n):
    if n<=1:
        return n
    return nFibo(n-1) + nFibo(n-2)

x = []
for i in range(2,15):
    x.append(nFibo(i))

print (x)