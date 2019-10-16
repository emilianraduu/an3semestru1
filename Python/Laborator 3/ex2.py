def createKeyMap(charList):
    return {a:charList.count(a) for a in charList}

print (createKeyMap('Ana are mere.'))