import random
import numpy as np

labirint = [[1,1,0,0,1,1,0,0],
[0,0,0,0,0,0,0,0],
[0,0,1,0,0,0,1,0],
[0,1,1,0,0,1,1,1],
[0,0,0,0,0,1,0,1],
[0,1,0,1,0,1,0,0],
[0,0,1,1,0,0,0,0],
[0,0,0,0,0,0,0,0]]
g_final = (0,7)
b_final = (1,7)
lr = 0.31
gamma = 1
q = {}
na = {}
alpha = 0.47

for x in range(0,8):
    for y in range(0,8):
        q[(x,y)] = {'up':0,'right':0,'left':0,'down':0}
        na[(x,y)] = {'up':0,'right':0,'left':0,'down':0}

a = ['up','down','right','left']
directs = {'up':(1,0),'down':(-1,0),'right':(0,1),'left':(0,-1)}

def qLearning(qStart,dim):
    action = ''
    episodes = 50
    while episodes != 0:
        nr_its = 1000
        start = qStart
        while nr_its > 0:
            pr = random.uniform(0,1)
            n_start = start
            n_action = action
            if pr > alpha:
                goTo = ''
                max1 = -1000
                for i in a:
                    if max1 < q[start][i]:
                        max1 = q[start][i]
                        goTo = i
                n_Start = (start[0] + directs[goTo][0],start[1] + directs[goTo][1])
                n_action = goTo
            else:
                nr_i = random.randrange(4)
                n_start = (start[0] + directs[a[nr_i]][0],start[1] + directs[a[nr_i]][1])
                n_action = a[nr_i]
            action = n_action
            na[start][action] += 1
            if n_start[0] >= 0 and n_start[0] < dim and n_start[1] >= 0 and n_start[1] < dim:
                if(labirint[n_start[0]][n_start[1]] == 0):
                    max1 = -1000
                    for i in a:
                        if q[n_start][i] > max1:
                            max1 = q[n_start][i]
                    reward = 0
                    if n_start == b_final:
                        reward = -1
                    elif n_start == g_final:
                        reward = 1
                    else:
                        reward = -0.04    
                    q[start][action] = q[start][action] + lr*(reward + gamma*max1 - q[start][action])
                    if reward == 1 or reward == -1:
                        break
                    start = n_start
                else:
                    reward = -0.04
                    q[start][action] = q[start][action] + lr*(reward + gamma*q[start][action] - q[start][action])
            else:
                reward = -0.04
                q[start][action] = q[start][action] + lr*(reward + gamma*q[start][action] - q[start][action])
            nr_its -= 1
        episodes -= 1
    print(q[g_final])
    print(labirint[g_final[0]][g_final[1]])
    start = qStart
    path = []
    path.append(start)
    while start != g_final:
        max1 = -1000
        act = ''
        for i in a:
            if start[0] + directs[i][0] >=0 and start[0] + directs[i][0] < dim and start[1] + directs[i][1] >= 0 and start[1] + directs[i][1] < dim:
                if max1 < q[start][i] and labirint[start[0] + directs[i][0]][start[1] + directs[i][1]] == 0:
                    max1 = q[start][i]
                    act = i
        start = (start[0] + directs[act][0],start[1] + directs[act][1])
        path.append(start)
    print(path)
    

qLearning((7,4),8)