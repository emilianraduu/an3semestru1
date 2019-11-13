import sys


def is_different(cell_i, cell_j):
    result = cell_i != cell_j
    return result


def number_of_conflicts(sudoku, cell, value):
    count = 0
    for related_c in sudoku.related_cells[cell]:
        if len(sudoku.possibilities[related_c]) > 1 and value in sudoku.possibilities[related_c]:
            count += 1

    return count


def is_consistent(sudoku, assignment, cell, value):

    is_consistent = True
    for current_cell, current_value in assignment.items():
        if current_value == value and current_cell in sudoku.related_cells[cell]:
            is_consistent = False

    return is_consistent


def assign(sudoku, cell, value, assignment):
    assignment[cell] = value
    if sudoku.possibilities:
        forward_check(sudoku, cell, value, assignment)


def unassign(sudoku, cell, assignment):
    if cell in assignment:
        for (coord, value) in sudoku.pruned[cell]:
            sudoku.possibilities[coord].append(value)
        sudoku.pruned[cell] = []
        del assignment[cell]


def forward_check(sudoku, cell, value, assignment):
    for related_c in sudoku.related_cells[cell]:
        if related_c not in assignment:
            if value in sudoku.possibilities[related_c]:
                sudoku.possibilities[related_c].remove(value)
                sudoku.pruned[cell].append((related_c, value))


def fetch_sudokus(input):
    DEFAULT_SIZE = 81
    if (len(input) % DEFAULT_SIZE) != 0:
        print("ERROR : NOT MULTIPLE OF {}".format(DEFAULT_SIZE))
        sys.exit()
    else:
        formatted_input = input.replace(
            "X", "0").replace("#", "0").replace("@", "0")
        if not formatted_input.isdigit():
            print(
                "ERROR : ONLY THESE CHARACTERS ALLOWED: [1,9], 'X', '#' and '@'")
            sys.exit()
        else:
            return [formatted_input[i:i+DEFAULT_SIZE] for i in range(0, len(formatted_input), DEFAULT_SIZE)]


def print_grid(grid):
    output = ""
    count = 1
    row = 0

    for cell in grid:
        value = cell

        output += value + " "

        if count % 3 == 0 and count != 9:
            output += '| '

        if count >= 9:
            count = 0
            row += 1
            if row % 3 == 0 and row != 9:
                output += "\n----------------------\n"
            else:
                output += '\n'

        count += 1

    return output
