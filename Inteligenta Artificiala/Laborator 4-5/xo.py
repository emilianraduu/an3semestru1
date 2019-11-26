import numpy as np
import random


def create_board():
    return(np.array([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]))


def possibilities(board):
    l = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                l.append((i, j))
    return(l)


def heuristic(board):
    lineHeuristic = 0
    countOpponentLine = 0
    countMeLine = 0
    allHeuristics = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                countOpponentLine += 1
            if board[i][j] == 2:
                countMeLine += 1

        if countOpponentLine == 1:
            lineHeuristic += 1
        if countOpponentLine == 2:
            lineHeuristic += 10
        if countOpponentLine == 3:
            lineHeuristic += 100
        if countMeLine == 1:
            lineHeuristic -= 1
        if countMeLine == 2:
            lineHeuristic -= 10
        if countMeLine == 3:
            lineHeuristic -= 100
        if countMeLine + countOpponentLine == 3 or countOpponentLine + countMeLine == 0:
            lineHeuristic = 0
        allHeuristics.append(lineHeuristic)


def random_place(board, player):
    selection = possibilities(board)
    current_loc = random.choice(selection)
    board[current_loc] = player
    return(board)


def row_win(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[x, y] != player:
                win = False
                continue
        if win == True:
            return(win)
    return(win)


def col_win(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                continue
        if win == True:
            return(win)
    return(win)


def diag_win(board, player):
    win = True
    for x in range(len(board)):
        if board[x, x] != player and board[x, 2-x] != player:
            win = False
    return(win)


def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if (row_win(board, player) or
            col_win(board, player) or
                diag_win(board, player)):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner


def play_game():
    board, winner, counter = create_board(), 0, 1
    print(board)
    while winner == 0:
        for player in [1, 2]:
            if player == 1:
                board = random_place(board, player)
                print(str(counter) + " move")
                print(board)
                print()
                counter += 1
                winner = evaluate(board)
                if winner != 0:
                    break
            elif player == 2:
                try:
                    line = input('Line = ')
                    line = int(line)
                    if line > 2:
                        return -1
                    column = input('Column = ')
                    column = int(column)
                    if column > 2:
                        return -1
                    if board[line][column] == 0:
                        board[line][column] = 2
                    else:
                        print('Wrong choice!')
                        return -1
                    print(str(counter) + " move")
                    print(board)
                    print()
                    counter += 1
                    winner = evaluate(board)
                    if winner != 0:
                        break
                except:
                    return -1

    print(board)
    print()
    return(winner)


game = str(play_game())
if game == str(-99):
    print('Error')
elif game == str(-1):
    print('No winner')
else:
    print("Winner is: " + game)
