
class Knight:

    def __init__(self):
        self.border_width = None
        self.border_height = None
        self.placeholder = None
        self.grid = None
        self.axis_x = None
        self.axis_y = None
        self.possible_moves = None

    def visit_cell(self, x=None, y=None, marker="X"):  # this name is no longer make sense, maybe " set_mark or mark cell? "
        self.grid[-y][x - 1] = f'{(self.placeholder - 1) * " "}{str(marker)}'  # something like ___ or __ to "  X"

    def create_grid(self):
        try:
            self.border_width, self.border_height = [int(x) for x in input("Enter your board dimensions: ").split() if int(x) > 0]
        except ValueError:
            print("Invalid position!")
            return self.create_grid()
        self.placeholder = len(str(self.border_width * self.border_height))
        self.grid = [["_" * self.placeholder for _ in range(self.border_width)] for _ in range(self.border_height)]

    def set_starting_position(self):
        try:
            self.axis_x, self.axis_y = [int(x) for x in input("Enter the knight's starting position: ").split()]
            assert all([0 < self.axis_y < self.border_height + 1, 0 < self.axis_x < self.border_width + 1])
            # -y as actual beginning of our array is on hte top and starts with 0, and if to start from the end (-1) there is no need subtract 1
            """ positions should be marked as _X or __X (instead of X_ or _X_),"""
            self.visit_cell(self.axis_x, self.axis_y)
        except (ValueError, AssertionError):
            print("Invalid position!")
            return self.set_starting_position()

    def print_grid(self):
        # self.border_height is the same is row number
        border = f' {"-" * (self.border_width * (self.placeholder + 1) + 3)}'  # finally correct border!
        print(border)
        for i in range(0, self.border_height):
            # rethink this conception, adding spaces only if sise more than 9 x 9, ideally making separate rules for left and bottom borders as they are quite independent
            print(str(self.border_height - i) + "|", " ".join(self.grid[i]), "|")
        print(f"{border}\n"
              f"{' ' * (self.placeholder + 2)}{(self.placeholder * ' ').join((str(n) for n in range(1, self.border_width + 1)))}", "\n")

    def generate_moves(self):  # rename like "generate_moves" ? as this function is no longer print anything

        def generate_moves(current_pos=(self.axis_x, self.axis_y)) -> tuple:
            x, y = current_pos  # first number - for axis x and 2nd for asix y
            """The knight moves in an L-shape, so
            it has to move 2 squares horizontally and 1 square vertically,
            or
            2 squares vertically and 1 square horizontally."""

            _step_values = ((2, 1), (2, -1), (-2,  1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2))
            potential_moves = map(lambda array: (array[0] + x, array[1] + y), _step_values)  # generator of potential move coordinates

            # It is crucial to use 'and' operator here to make sure that values are within borders
            return tuple(_move for _move in potential_moves if all([0 < _move[0] <= self.border_width and 0 < _move[1] <= self.border_height
                                                                    and self.grid[-_move[1]][_move[0]-1][-1] not in {"*", "X"}]
                                                                   )
                         )

        self.possible_moves = generate_moves()
        for move in self.possible_moves:
            self.visit_cell(x=move[0], y=move[1], marker=str(len(generate_moves(move))))

    def make_move(self, message="Enter your next move: "):
        try:
            _x, _y = [int(x) for x in input(message).split()]
            assert (_x, _y) in self.possible_moves
        except (AssertionError, ValueError):
            return self.make_move(message="Invalid move! Enter your next move: ")

        self.visit_cell(self.axis_x, self.axis_y, marker="*")  # marking current position with asterisk

        self.axis_x, self.axis_y = _x, _y  # reassigning position to new values

        self.visit_cell(self.axis_x, self.axis_y, marker="X")  # moving current position to _x, _y coordinates

        self.remove_old_marks()  # removing old digits from the grid
        # set new marks with self.generate_moves()
        self.generate_moves()

    def remove_old_marks(self):
        for move in self.possible_moves:
            if (move[0], move[1]) != (self.axis_x, self.axis_y):
                self.visit_cell(move[0], move[1], marker="_")


def main():
    knight = Knight()
    knight.create_grid()
    knight.set_starting_position()
    knight.generate_moves()  # maybe re-name to "current board status"?
    knight.print_grid()

    while knight.possible_moves:
        knight.make_move()
        knight.print_grid()

    empty_cells = tuple(cell for row in knight.grid for cell in row if cell[-1] == "_")
    print("What a great tour! Congratulations!" if not empty_cells else f"No more possible moves!\nYour knight visited {len(tuple(cell for row in knight.grid for cell in row if cell[-1] in {'*', 'X'}))} squares!")


if __name__ == '__main__':
    main()
#  Note that the board is guaranteed to have a solution if the smallest dimension is at least 5. Smaller boards may not have a solution.
