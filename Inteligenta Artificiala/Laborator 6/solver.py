import argparse
import sys
from sudoku import Sudoku
from ac3 import AC3
from backtrack import recursive_backtrack_algorithm
from utils import fetch_sudokus, print_grid

sudokus = dict(
    easy="000079065000003002005060093340050106000000000608020059950010600700600000820390000",
    medium="102004070000902800009003004000240006000107000400068000200800700007501000080400109",
    hard="002008050000040070480072000008000031600080005570000600000960048090020000030800900")


def solve(grid, index, total):
    print("{}".format(print_grid(grid)))

    sudoku = Sudoku(grid)

    AC3_result = AC3(sudoku)

    if not AC3_result:
        print("NO SOLUTION")

    else:
        if sudoku.isFinished():
            print("RESULT \n\n{}".format(sudoku))
        else:
            print("START BKT")

            assignment = {}

            for cell in sudoku.cells:
                if len(sudoku.possibilities[cell]) == 1:
                    assignment[cell] = sudoku.possibilities[cell][0]

            assignment = recursive_backtrack_algorithm(assignment, sudoku)

            for cell in sudoku.possibilities:
                sudoku.possibilities[cell] = assignment[cell] if len(
                    cell) > 1 else sudoku.possibilities[cell]

            if assignment:
                print("RESULT \n\n{}".format(sudoku))

            else:
                print("NO SOLUTION")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Solve Sudoku')
    parser.add_argument(
        '--string', type=str, help='sudoku as a String, can be multiple sudokus in a row in the same line')
    parser.add_argument('--level', type=str, default='medium', choices=[
                        'easy', 'medium', 'hard'], help='selects default sudoku\'s based on level (default: %(default)s)')
    args = parser.parse_args()

    sudoku_grid_as_string = ""

    if not args.string:
        sudoku_grid_as_string = sudokus[args.level]
        print("\nLEVEL : {}\n".format(args.level.upper()))
    else:
        sudoku_grid_as_string = args.string

    sudoku_queue = fetch_sudokus(sudoku_grid_as_string)

    for index, sudoku_grid in enumerate(sudoku_queue):
        solve(sudoku_grid, index + 1, len(sudoku_queue))
