import sys

sys.setrecursionlimit(200)


class Board:
    def __init__(self):
        self.border_width = None
        self.border_height = None
        self.placeholder = None
        self.grid = None

    def board_params(self):
        try:
            self.border_width, self.border_height = [int(x) for x in input("Enter your board dimensions: ").split() if
                                                     int(x) > 0]
        except ValueError:
            print("Invalid position!")
            return self.board_params()


    def create_board(self, w=None, h=None):
        if not all([w, h]):
            w = self.border_width
            h = self.border_height

        self.placeholder = len(str(w * h))
        self.grid = [["_" * self.placeholder for _ in range(w)] for _ in range(h)]

    def print_grid(self):
        # self.border_height is the same is row number
        border = "-" * (self.border_width * (self.placeholder + 1) + 3)  # finally correct border!
        print(border)
        for i in range(0, self.border_height):
            # rethink this conception, adding spaces only if sise more than 9 x 9, ideally making separate rules for left and bottom borders as they are quite independent
            print(str(self.border_height - i) + "|", " ".join(self.grid[i]), "|")
        print(f"{border}\n"
              f"{' ' * (self.placeholder + 2)}{(self.placeholder * ' ').join((str(n) for n in range(1, self.border_width + 1)))}",
              "\n")


class Knight:

    def __init__(self, board):
        self.axis_x = None
        self.axis_y = None
        self.possible_moves = None
        self.board = board
        self.move_limitations = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (2, 1), (1, 2), (1, -2), (2, -1)]
        self.x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
        self.y_moves = [1, 2, 2, 1, -1, -2, -2, -1]

    def visit_cell(self, x=None, y=None,
                   marker="X"):  # this name is no longer make sense, maybe " set_mark or mark cell? "
        self.board.grid[-y][
            x - 1] = f'{(self.board.placeholder - 1) * " "}{str(marker)}'  # something like ___ or __ to "  X"

    def validate_starting_position(self):
        try:
            self.axis_x, self.axis_y = [int(x) for x in input("Enter the knight's starting position: ").split()]
            assert all([0 < self.axis_y < self.board.border_height + 1, 0 < self.axis_x < self.board.border_width + 1])
            # -y as actual beginning of our array is on hte top and starts with 0, and if to start from the end (-1) there is no need subtract 1
            """ positions should be marked as _X or __X (instead of X_ or _X_),"""
            return True
        except (ValueError, AssertionError):
            print("Invalid position!")
            return self.validate_starting_position()

    def is_valid_move(self, _x, _y):

        return all([0 < _x <= self.board.border_width and 0 < _y <= self.board.border_height
                    and self.board.grid[-_y][_x - 1][-1] == "_"])  # not in "*X"

    def generate_moves(self, x, y):  # rename like "generate_moves" ? as this function is no longer print anything

        potential_moves = map(lambda array: (array[0] + x, array[1] + y),
                              self.move_limitations)  # generator of potential move coordinates

        # It is crucial to use 'and' operator here to make sure that values are within borders
        return tuple(_move for _move in potential_moves if self.is_valid_move(_move[0], _move[1]))

    def display_possible_moves(self):
        for move in self.possible_moves:
            self.visit_cell(x=move[0], y=move[1], marker=str(len(self.generate_moves(move[0], move[1]))))

    def make_move(self, message="Enter your next move: "):
        try:
            _x, _y = [int(x) for x in input(message).split()]
            assert (_x, _y) in self.possible_moves
        except (AssertionError, ValueError):
            return self.make_move(message="Invalid move! Enter your next move: ")

        self.visit_cell(self.axis_x, self.axis_y, marker="*")  # marking current position with asterisk

        self.visit_cell(_x, _y, marker="X")  # moving current position to _x, _y coordinates
        self.axis_x, self.axis_y = _x, _y  # reassigning position to new values

        self.remove_old_marks()  # removing old digits from the grid
        # set new marks with self.generate_moves()

        # make it property
        self.possible_moves = self.generate_moves(_x, _y)
        self.display_possible_moves()

    def remove_old_marks(self):
        for move in self.possible_moves:
            if (move[0], move[1]) != (self.axis_x, self.axis_y):
                self.visit_cell(move[0], move[1], marker="_")

    def solve_game(self, x, y, counter):
        for i in range(8):

            if counter >= self.board.border_width * self.board.border_height + 1:
                return True
            new_x = x + self.x_moves[i]
            new_y = y + self.y_moves[i]

            if self.is_valid_move(new_x, new_y):
                self.visit_cell(new_x, new_y, counter if counter >= 10 else f"{0}{counter}")

                if self.solve_game(new_x, new_y, counter + 1):
                    return True

                self.visit_cell(new_x, new_y, "__")
        return False

    def reset_board(self):
        w, h = self.board.border_width, self.board.border_height
        board = Board()
        board.border_width = w
        board.border_height = h
        board.create_board(w, h)
        self.board = board
        #self.board.print_grid()


    def start_game(self):
        # need to create one more table to play with it
        # if moved to cell and no possible moves from there - return False.

        start = input("Do you want to try the puzzle? (y/n): ")
        match start:
            case "y":
                self.visit_cell(self.axis_x, self.axis_y, marker="01")
                a = self.solve_game(self.axis_x, self.axis_y, 2)
                print(a)
                if not a:
                    print("No solution exists!")
                    exit()
                else:
                    self.board.print_grid()
                    self.reset_board()
                    self.visit_cell(self.axis_x, self.axis_y, marker="X")

            case "n":
                self.visit_cell(self.axis_x, self.axis_y, marker="01")
                if self.solve_game(self.axis_x, self.axis_y, 2):
                    print("Here's the solution!")
                    self.board.print_grid()
                    exit()
                else:
                    #self.board.print_grid()
                    print("No solution exists!")
                    exit()
            case _:
                print("Invalid input!")
                return self.start_game()


def main():
    board = Board()
    board.board_params()
    board.create_board()

    knight = Knight(board)
    knight.validate_starting_position()

    knight.start_game()

    knight.possible_moves = knight.generate_moves(knight.axis_x, knight.axis_y)

    knight.display_possible_moves()  # maybe re-name to "current board status"?
    #print('line #178')
    knight.board.print_grid()

    while knight.possible_moves:
        knight.make_move()
        knight.board.print_grid()

    empty_cells = tuple(cell for row in knight.board.grid for cell in row if cell[-1] == "_")
    print(
        "What a great tour! Congratulations!" if not empty_cells else f"No more possible moves!\nYour knight visited {len(tuple(cell for row in knight.board.grid for cell in row if cell[-1] in {'*', 'X'}))} squares!")


if __name__ == '__main__':
    main()
#  Note that the board is guaranteed to have a solution if the smallest dimension is at least 5. Smaller boards may not have a solution.
