import random
from itertools import combinations


def checkValidity(item):
    if item.count('m') != 0 and item.count('m') < item.count('c'):
        return False
    return True


def getPosibilities(state):
    boatPosibility = []
    if state['boat'][0] == 1:
        if state['boat'].count(0) <= len(state['m1'])-1:
            for options in combinations(state['m1'], state['boat'].count(0)):
                if checkValidity(options):
                    boatPosibility.append(options)
        else:
            for options in state['m1']:
                boatPosibility.append(options)
    else:
        random.choice(state['m2'])
    print (boatPosibility)
    return list(random.choice(boatPosibility))


def moveBoat(state):
    if state['boat'][0] == 1:
        state['boat'][0] == 2
    else:
        state['boat'][0] == 1


def insertInBoat(state, persons):
    shore = 'm' + str(state['boat'][0])
    personIndex = 0
    for index, item in enumerate(state['boat']):
        if item == 0:
            print(personIndex)
            print(persons)
            if persons[personIndex]:
                state['boat'][index] = persons[personIndex]
                personIndex += 1
    personIndex = 0
    for item in state[shore]:
        for option in persons:
            if item == option:
                state[shore].remove(item)
    return state


def removeFromBoat(state):
    shore = 'm' + str(state['boat'][0])
    if shore == 'm1':
        shore = 'm2'
    else:
        shore = 'm1'

    for item in state['boat']:
        if item != 1 and item != 2:
            state[shore].append(item)

    for index in range(1, len(state['boat'])):
        state['boat'][index] = 0
    return state


def checkFinal(state):
    if state['boat'][0] == 2 and len(state['m1']) == 0:
        return True
    return False


def startGame(state):
    if checkValidity(state['m1']):
        while checkFinal(state) == False:
            state = insertInBoat(state, getPosibilities(state))
            state = removeFromBoat(state)
            print(state)
    else:
        return 0


def initialization():
    m1 = []
    m2 = []
    boat = [1]
    noCanibals = int(input('Canibals:'))
    noMissionaries = int(input('Missionaries:'))
    boatCapacity = int(input('Boat capacity:'))

    if noCanibals > noMissionaries or boatCapacity < 1:
        return False

    for i in range(0, noCanibals):
        m1.append('c')

    for i in range(0, noMissionaries):
        m1.append('m')

    for i in range(0, boatCapacity):
        boat.append(0)

    initialState = {'m1': m1, 'm2': m2, 'boat': boat, 'visited': True}

    startGame(initialState)


initialization()
