# array = [[(x, y) for x in range(1, 9)] for y in range(8, 0, -1)]

import re

class Knight:

    def __init__(self):
        self.border_width = None
        self.border_height = None
        self.placeholder = None
        self.grid = None
        self.axis_x = None
        self.axis_y = None
        self.possible_moves = None
        self.temp_x = None
        self.temp_y = None

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
            if not all([0 < self.axis_y < self.border_height + 1, 0 < self.axis_x < self.border_width + 1]):
                print("Invalid position!")
                return self.set_starting_position()
            # -y as actual beginning of our array is on hte top and starts with 0, and if to start from the end (-1) there is no need subtract 1
            """ positions should be marked as _X or __X (instead of X_ or _X_),"""
            self.visit_cell(self.axis_x, self.axis_y)

        except ValueError:
            print("Invalid position!")
            return self.set_starting_position()

    def print_grid(self):
        row_n = self.border_height
        border = f' {"-" * (self.border_width * (self.placeholder + 1) + 3)}'  # finally correct border!
        print(border)
        for i in range(0, row_n):
            # rethink this conception, adding spaces only if sise more than 9 x 9, ideally making separate rules for left and bottom borders as they are quite independent
            print(str(row_n) + "|", " ".join(self.grid[i]), "|")
            row_n -= 1
        print(border)
        print(f"{' ' * (self.placeholder + 2)}{(self.placeholder * ' ').join((str(n) for n in range(1, self.border_width + 1)))}", "\n")

    def show_moves(self):  # rename like "generate_moves" ? as this function is no longer print anything

        def generate_moves(current_pos=(self.axis_x, self.axis_y)) -> tuple:
            x, y = current_pos  # first number - for axis x and 2nd for asix y
            """The knight moves in an L-shape, so
            it has to move 2 squares horizontally and 1 square vertically,
            or
            2 squares vertically and 1 square horizontally."""

            all_potential_moves = ((2, 1), (2, -1), (-2,  1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2))

            potential_moves = map(lambda array: (array[0] + x, array[1] + y), all_potential_moves)  # generator

            # SETTING ADDITIONAL FILTERS TO MAKE SURE THAT ORIGINAL POINT IS NOT INCLUDED.
            potential_moves = tuple(_move for _move in potential_moves if 0 < _move[0] <= self.border_width and 0 < _move[1] <= self.border_height and (_move[0], _move[1]) != (x, y) and self.grid[-_move[1]][_move[0]-1][-1] != "*" and (_move[0], _move[1]) != (self.axis_x, self.axis_y) and (_move[0], _move[1]) != (self.temp_x, self.temp_y))
            return potential_moves

        self.possible_moves = generate_moves()

        # maybe implement temp position here and add filter into the next line?
        self.possible_moves = tuple([x for x in self.possible_moves if len(generate_moves(x)) >= 0])

        # need to filter current position.

        for move in self.possible_moves:
            # __FIXED__ "marker=str(move[2] - 1)" Minus one because each list includes so=called " step back to original place,
            self.visit_cell(x=move[0], y=move[1], marker=str(len(generate_moves(move))))  # in latter stage filter if cell != '*' will be needed
        # print("Here are the possible moves:")

    def make_move(self, message="Enter your next move: "):

        # print(next_move)
        # try to assign, if success change current market and reassing asix
        try:
            _x, _y = [int(x) for x in input(message).split()]

            """ make sure move in potential moves"""
            # check if move is possible

            if not re.match(r"\A\d$", self.grid[-_y][_x-1][-1]):   # last symbol
                raise IndexError
        except (IndexError, ValueError):
            return self.make_move(message="Invalid move! Enter your next move: ")

        self.temp_x, self.temp_y = self.axis_x, self.axis_y  # setting position before move to temp variables

        self.visit_cell(self.axis_x, self.axis_y, marker="*")  # marking current position with asterisk

        self.axis_x, self.axis_y = _x, _y  # reassigning position to new values

        self.visit_cell(self.axis_x, self.axis_y, marker="X")  # moving current position to _x, _y coordinates

        self.remove_old_marks()  # removing old digits from the grid
        # set new marks with self.show_moves()
        self.show_moves()


    """ create check two int function"""

    def remove_old_marks(self):
        for row in range(self.border_height):
            for element in range(len(self.grid[row])):
                #print(f'"{self.grid[row][element]}"')
                # self.grid[row][element][-1] = re.sub(r"\d", "_", self.grid[row][element][-1])
                #self.grid[row][element] = self.grid[row][element].replace(self.grid[row][element][-1], "_")
                if re.match(r"\A\d$", self.grid[row][element][-1]):
                    self.grid[row][element] = "_" * self.placeholder





def main():
    knight = Knight()
    knight.create_grid()
    knight.set_starting_position()
    knight.show_moves()  # maybe re-name to "current board status"?
    knight.print_grid()





    while knight.possible_moves:
        knight.make_move()
        knight.print_grid()


    #print("sorry, no more steps availiable")
    empty_cells = [cell for row in knight.grid for cell in row if cell[-1] == "_"]

    if not empty_cells:
        print("What a great tour! Congratulations!")
    else:
        visited_cells = [cell for row in knight.grid for cell in row if cell[-1] in {"*", "X"}]  # or just +1 ?
        print(f"No more possible moves!\nYour knight visited {len(visited_cells)} squares!")




if __name__ == '__main__':
    main()
#  Note that the board is guaranteed to have a solution if the smallest dimension is at least 5. Smaller boards may not have a solution.
