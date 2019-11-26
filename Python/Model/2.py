def problema2(n,m):
    z = m
    result_list = []
    while z>1:
        z = m - 2*n
        m = n
        n = z
        result_list.append(z)
    result_list = result_list[::-1]
    return tuple(result_list[:2])
print(problema2(41,99))