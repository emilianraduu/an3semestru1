def problema1(n):
    sum = 0
    for i in range(1,n+1):
        sum+=i
    return(sum)


def problema5(n):
    return str(int(n,8))==str(int(n,8))[::-1]

