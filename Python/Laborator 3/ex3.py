a = {'a': 12, 'b': 15, 'd': [1,2,3]}
b = {'b': 15, 'd' : [1,2,3]}

print('Comp')
print(len({value: a[value] for value in a if value in b and a[value] == b[value]})==0)
print('Common keys')
print(list({value: a[value] for value in a if value in b and a[value] != b[value]}))
print('In a but not in b')
print ([value for value in a if value not in b])
print('In b but not in a')
print ([value for value in b if value not in a])