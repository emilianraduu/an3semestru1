from utils import number_of_conflicts

def select_unassigned_variable(assignment, sudoku):
    unassigned = []
    for cell in sudoku.cells:
        if cell not in assignment:
            unassigned.append(cell)

    criterion = lambda cell: len(sudoku.possibilities[cell])
    return min(unassigned, key=criterion)

def order_domain_values(sudoku, cell):
    if len(sudoku.possibilities[cell]) == 1:
        return sudoku.possibilities[cell]

    criterion = lambda value: number_of_conflicts(sudoku, cell, value)
    return sorted(sudoku.possibilities[cell], key=criterion)