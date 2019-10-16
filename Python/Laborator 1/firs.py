def gdc(a,b):
    if a==b:
        return a
    else:
        if a>b:
            gdc(a-b,b)
        else:
            gdc(a,b-a)


print('a=')
a=int(input())
print('b=')
b=int(input())
print (gdc(a,b))