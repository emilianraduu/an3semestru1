q = {}
na = {}

def initialize_q_table(MATRIX_SIZE):
    for x in range(0,MATRIX_SIZE):
        for y in range(0,MATRIX_SIZE):
            q[(x,y)] = {'up':0,'right':0,'left':0,'down':0}
            na[(x,y)] = {'up':0,'right':0,'left':0,'down':0}
    return (q,na)