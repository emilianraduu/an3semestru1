# IMPORTS
import random
import time
f = open('out.txt', 'a+')

# CONSTANTS
MAX_COUNT = 1500

# INITIALIZATION
state = []
visited = {}
previous = {}
progressStates = {}


def clearData():
    visited.clear()
    previous.clear()
    progressStates.clear()


def initialization(noMissionaries, noCannibals):
    return [noCannibals, noMissionaries, 0, 0, 0]


# MAX FUNCTION
def maximum(a, b):
    if a > b:
        return a
    else:
        return b


# VALIDATIONS
def finalStateValidation(state, noCannibals, noMissionaries):
    if state == [0, 0, 1, noCannibals, noMissionaries]:
        return True
    return False


def isValidTransition(state, movingCannibals, movingMissionaries, noCannibals, noMissionaries, boatCapacity):
    if movingCannibals == 0 and movingMissionaries == 0:
        return False
    if movingCannibals > movingMissionaries and movingMissionaries != 0:
        return False

    val1 = state[0] + int((-1)**(1-state[2])) * movingCannibals
    val2 = state[3] + int((-1)**state[2]) * movingCannibals
    val3 = state[1] + int((-1)**(1-state[2])) * movingMissionaries
    val4 = state[4] + int((-1)**state[2]) * movingMissionaries

    if state[2] == 0 and (movingCannibals > state[0] or movingMissionaries > state[1]):
        return False
    elif state[2] == 1 and (movingCannibals > state[3] or movingMissionaries > state[4]):
        return False
    if (val1 > val3 and val3 != 0) or (val2 > val4 and val4 != 0) or (movingCannibals+movingMissionaries > boatCapacity):
        return False
    if val1 < 0 or val2 < 0 or val3 < 0 or val4 < 0 or val1 > noCannibals or val2 > noCannibals or val3 > noMissionaries or val4 > noMissionaries:
        return False
    return True


# TRANSITIONS
def transition(state, movingCannibals, movingMissionaries):
    state[2] = 1 - state[2]
    state[0] = state[0] + (-1)**state[2] * movingCannibals
    state[3] = state[3] + (-1)**(1-state[2]) * movingCannibals
    state[1] = state[1] + (-1)**state[2] * movingMissionaries
    state[4] = state[4] + (-1)**(1-state[2]) * movingMissionaries
    return state


def generate_transitions(number_of_missionaries, number_of_cannibals, boatCapacity):
    transitions = []
    for i in range(number_of_missionaries):
        for j in range(number_of_cannibals):
            if (i != 0 or j != 0) and (i+j <= boatCapacity):
                transitions.append((i, j))
    return transitions


# RANDOM STRATEGY
def randomStrategy(state, totalCannibals, totalMissionaries, boatCapacity):
    contor = 0
    visited[str(state)] = 1
    initialState = state.copy()
    contorFailed = 0
    acceptedStates = []
    while not finalStateValidation(state, totalCannibals, totalMissionaries) and contorFailed < MAX_COUNT:
        if contor >= MAX_COUNT:
            contor = 0
            contorFailed += 1

            state = initialState.copy()

            visited.clear()
            visited[str(state)] = 1

            acceptedStates.clear()
        else:
            contor += 1

        numMissionaries = -1
        numCannibals = -1

        if state[2] == 0:
            numMissionaries = random.randrange(0, state[1]+1)
            numCannibals = random.randrange(0, maximum(
                boatCapacity - numMissionaries, state[0])+1)
        else:
            numMissionaries = random.randrange(0, state[4]+1)
            numCannibals = random.randrange(0, maximum(
                boatCapacity - numMissionaries, state[3])+1)

        if isValidTransition(state, numCannibals, numMissionaries, totalCannibals, totalMissionaries, boatCapacity):
            c_state = state.copy()
            new_State = transition(c_state, numCannibals, numMissionaries)
            if str(new_State) not in visited:
                visited[str(new_State)] = 1
                state = new_State
                acceptedStates.append(state)
    if finalStateValidation(state, totalCannibals, totalMissionaries) == True:
        # for states in acceptedStates:
        print('Random steps: ', contor, file=f)


# BKT ALGORITHM
def bkt(transitions, states, position, boatCapacity, found=False):
    if found == False:
        if finalStateValidation(states[position-1], states[0][0], states[0][1]):
            print('BKT STEPS:', position, file=f)
            bkt(transitions, states, position+1, boatCapacity, True)
        else:
            for trans in transitions:
                if isValidTransition(states[position-1], trans[1], trans[0], states[0][0], states[0][1], boatCapacity):
                    current_state = states[position-1].copy()
                    new_state = transition(current_state, trans[1], trans[0])
                    if new_state not in states:
                        if len(states) <= position:
                            states.append(new_state)
                        else:
                            states[position] = new_state
                        bkt(transitions, states, position+1, boatCapacity)
    else:
        return 0


def prep_bkt(state, boatCapacity):
    transitions = generate_transitions(state[1], state[0], boatCapacity)
    states = [state]
    bkt(transitions, states, 1, boatCapacity)


# HEURISTIC
def heuristic(state, boatCapacity):
    return state[0] + state[1]


# A* ALGORITHM
def aStar(state, totalCannibals, totalMissionaries, boatCapacity):
    openList = []
    openList.append(state)
    visited[str(state)] = 0
    previous[str(state)] = 0
    progressStates[str(state)] = -1
    while openList:
        openList.sort(key=lambda el: previous[str(el)])
        st = openList.pop(0)
        for x in range(0, boatCapacity+1):
            for y in range(0, boatCapacity-x+1):
                if isValidTransition(st, y, x, totalCannibals, totalMissionaries, boatCapacity) == True:
                    n_state = st.copy()
                    n_state = transition(n_state, y, x)

                    if str(n_state) not in visited:
                        visited[str(n_state)] = visited[str(st)] + 1
                        previous[str(n_state)] = heuristic(
                            n_state, boatCapacity)
                        openList.append(n_state)
                        progressStates[str(n_state)] = str(st)
                        if finalStateValidation(n_state, totalCannibals, totalMissionaries):
                            print('A* steps: ', len(previous), file=f)
                            return
                    else:
                        if visited[str(st)] + 1 <= visited[str(n_state)]:
                            visited[str(n_state)] = visited[str(st)] + 1
                            previous[str(n_state)] = heuristic(
                                n_state, boatCapacity)
                            progressStates[str(n_state)] = str(st)
                            if finalStateValidation(n_state, totalCannibals, totalMissionaries):
                                print('A* steps: ', len(previous), file=f)
                                return
                            if n_state not in openList:
                                openList.append(n_state)
    return


def solve():
    meanRandom = 0
    meanBKT = 0
    meanAStar = 0
    for i in range(0, 10):
        try:
            noMissionaries = int(input('Number of missionaries: '))
            noCannibals = int(input('Number of cannibals: '))
        except:
            return 0

        while noCannibals > noMissionaries:
            noCannibals = int(input(
                'The number of cannibals must be smaller or equal than the number of missionaries: '))

        try:
            boatCapacity = int(input('Boat capacity: '))
        except:
            return 0

        state = initialization(noMissionaries, noCannibals)


        print('STEP:', i+1, file=f)
        print('STATE:', state, file=f)
        print('', file=f)

        start = time.time()
        randomStrategy(state, noCannibals, noMissionaries, boatCapacity)
        end = time.time()
        meanRandom = meanRandom + end-start
        print('Random strategy:', end-start, 's', file=f)
        print('', file=f)

        clearData()
        state = initialization(noMissionaries, noCannibals)

        start = time.time()
        prep_bkt(state, boatCapacity)
        end = time.time()
        print('BKT strategy:', end-start, 's', file=f)
        meanBKT = meanBKT + end-start
        print('', file=f)

        clearData()
        state = initialization(noMissionaries, noCannibals)

        start = time.time()
        aStar(state, noCannibals, noMissionaries, boatCapacity)
        end = time.time()
        print('A* Strategy:', end-start, 's', file=f)
        meanAStar = meanAStar + end-start
        print('', file=f)
        print('', file=f)

    meanRandom = meanRandom / 10
    meanBKT = meanBKT / 10
    meanAStar = meanAStar / 10

    print('Media Random', meanRandom,file=f)
    print('Media BKT', meanBKT,file=f)
    print('Media AStar', meanAStar,file=f)

solve()
