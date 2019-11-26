import random
from itertools import combinations


def checkValidity(item):
    if item.count('m') != 0 and item.count('m') < item.count('c'):
        return False
    return True


def getPosibilities(state):
    boatPosibility = []
    if state['boat'][0] == 1:
        if state['boat'].count(0) <= len(state['m1']):
            for options in combinations(state['m1'], state['boat'].count(0)):
                if checkValidity(options):
                    boatPosibility.append(options)
        else:
            for options in state['m1']:
                boatPosibility.append(options)
            return boatPosibility
    elif state['boat'][0]==2:
        return random.choice(state['m2'])
    return list(random.choice(boatPosibility))


def insertInBoat(state, persons):
    boatIndex = 1
    print(persons)
    for item in persons:
        if state['boat'][boatIndex] == 0:
            state['boat'][boatIndex] = item
            boatIndex += 1
            state['m'+str(state['boat'][0])].remove(item)
    
    if state['boat'][0]==1:
        state['boat'][0]=2
    else:
        state['boat'][0]=1
    return state


def removeFromBoat(state):
    shore = 'm' + str(state['boat'][0])
    for index, item in enumerate(state['boat']):
        if item != 0 and index != 0:
            state[shore].append(item)
            state['boat'][index] = 0
    return state


def makeMove(state):
    newState = {}
    newState = insertInBoat(state, getPosibilities(state))
    newState = removeFromBoat(state)
    print(newState)
    return newState


def checkFinal(state):
    if state['boat'][0] == 2 and len(state['m1']) == 0:
        return True
    return False


def startGame(state):
    visitedStates = []
    if checkValidity(state['m1']) and checkValidity(state['m2']):
        while checkFinal(state) == False:
            state = makeMove(state)
            visitedStates.append(state)
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
