import operator


def sortByFirstName(tuple):
    tuple.sort(key=operator.itemgetter(1))
    return tuple


array = [('radu', 'emi'), ('gatu', 'cristian'), ('ichim', 'teodora')]

print(sortByFirstName(array))
