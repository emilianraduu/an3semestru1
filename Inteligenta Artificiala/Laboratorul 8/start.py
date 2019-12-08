from readFile import read
from initialize import initialize_q_table
import random
import numpy

labirint = read()

MATRIX_SIZE = len(labirint[0])

SUCCESS_EXIT = (0,0)
BUST_EXIT = (1,0)
START_POS = (3,3)

LEARNING_RATE = 0.7
PENALTY = 0.05

a = ['up','down','right','left']
DIRECTIONS = {'up':(1,0),'down':(-1,0),'right':(0,1),'left':(0,-1)}

NR_STEPS = 500
NR_EPISODES = 30

epsilon = 1

(q,na) = initialize_q_table(MATRIX_SIZE)

def qLearning(qStart,dim):
    action = ''
    episodes = NR_EPISODES
    eps = epsilon
    while episodes != 0:
        nr_its = NR_STEPS
        start = qStart

        while nr_its > 0:
            pr = random.uniform(0,1)
            n_start = start
            n_action = action

            if pr > eps:
                goTo = ''
                max1 = -NR_STEPS
                for i in a:
                    if max1 < q[start][i]:
                        max1 = q[start][i]
                        goTo = i
                n_start = (start[0] + DIRECTIONS[goTo][0],start[1] + DIRECTIONS[goTo][1])
                n_action = goTo
            else:
                eps -= PENALTY
                random_move = random.randrange(4)
                n_start = (start[0] + DIRECTIONS[a[random_move]][0],start[1] + DIRECTIONS[a[random_move]][1])
                n_action = a[random_move]

            action = n_action
            na[start][action] += 1

            if n_start[0] >= 0 and n_start[0] < dim and n_start[1] >= 0 and n_start[1] < dim:
                if(labirint[n_start[0]][n_start[1]] == 0):
                    max1 = -NR_STEPS
                    for i in a:
                        if q[n_start][i] > max1:
                            max1 = q[n_start][i]
                    reward = 0
                    if n_start == BUST_EXIT:
                        reward = -1
                    elif n_start == SUCCESS_EXIT:
                        reward = 1
                    else:
                        reward = -PENALTY  
                    q[start][action] = q[start][action] + LEARNING_RATE*(reward + epsilon*max1 - q[start][action])
                    if reward == 1 or reward == -1:
                        break
                    start = n_start
                else:
                    reward = -PENALTY
                    q[start][action] = q[start][action] + LEARNING_RATE*reward
            else:
                reward = -PENALTY
                q[start][action] = q[start][action] + LEARNING_RATE*reward
            
            nr_its -= 1

        episodes -= 1
    print('LEARNING FINISHED')

    start = qStart
    path = []
    path.append(start)
    while start != SUCCESS_EXIT:
        max1 = -NR_STEPS
        act = ''
        for i in a:
            if start[0] + DIRECTIONS[i][0] >=0 and start[0] + DIRECTIONS[i][0] < dim and start[1] + DIRECTIONS[i][1] >= 0 and start[1] + DIRECTIONS[i][1] < dim:
                if max1 < q[start][i] and labirint[start[0] + DIRECTIONS[i][0]][start[1] + DIRECTIONS[i][1]] == 0:
                    max1 = q[start][i]
                    act = i
        start = (start[0] + DIRECTIONS[act][0],start[1] + DIRECTIONS[act][1])
        path.append(start)
    print(path)


qLearning(START_POS, MATRIX_SIZE)