def checkFirstName(array, firstName):
    ok = False
    for item in array:
        if item[1] == firstName:
            ok = True

    return ok


array = [('radu', 'emi'), ('gatu', 'cristian'), ('ichim', 'teodora')]

print(checkFirstName(array, 'em'))
