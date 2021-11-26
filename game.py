# array = [[(x, y) for x in range(1, 9)] for y in range(8, 0, -1)]

class Knight:

    def __init__(self):
        self.border_width = None
        self.border_height = None
        self.placeholder = None
        self.grid = None
        self.axis_x = None
        self.axis_y = None
        self.temporary_grid = None
        self.current_pos = None


    def visit_cell(self, x=None, y=None, marker="X", temp=False):
        if not temp:
            grid = self.grid
            y = self.axis_y
            x = self.axis_x
        else:
            grid = self.temporary_grid
            marker = "O"

        grid[-y][x - 1] = (self.placeholder - 1) * " " + marker  # something like ___ or __ to "  X"


    def create_grid(self):
        try:
            self.border_width, self.border_height = [int(x) for x in input("Enter your board dimensions: ").split() if int(x) >= 0]
        except ValueError:
            print("Invalid position!")
            return self.create_grid()

        self.placeholder = len(str(self.border_width * self.border_height))
        self.grid = [["_" * self.placeholder for _ in range(self.border_width)] for _ in range(self.border_height)]

    def set_starting_position(self):
        pos = input("Enter the knight's starting position: ")
        try:
            self.axis_x, self.axis_y = [int(x) for x in pos.split()]
            if not all([0 < self.axis_y < self.border_height + 1, 0 < self.axis_x < self.border_width + 1]):
                print("Invalid position!")
                return self.set_starting_position()
            # -y as actual beginning of our array is on hte top and starts with 0, and if to start from the end (-1) there is no need subtract 1
            """ positions should be marked as _X or __X (instead of X_ or _X_),"""

            self.visit_cell()

        except ValueError:
            print("Invalid position!")
            return self.set_starting_position()

    def print_grid(self, temp=False):

        if not temp:
            printable_grid = self.grid
        else:
            printable_grid = self.temporary_grid

        row_n = self.border_height
        border_length = self.border_width * (self.placeholder + 1) + 3
        border = " " + "-" * border_length  # finally correct border!
        print(border)

        for i in printable_grid:
            # rethink this conception, adding spaces only if sise more than 9 x 9, ideally making separate rules for left and bottom borders as they are quite independent
            print(str(row_n) + "|", " ".join(i), "|")
            row_n -= 1
        print(border)
        print(' ' * (self.placeholder + 2) + (self.placeholder * " ").join([str(n) for n in range(1, self.border_width + 1)]))
        print()

    def show_moves(self):
        # think about copy object, so not to reset marks each time
        self.temporary_grid = self.grid  # need to fix, as print function is hard coded for self.grid
        # checking what moves are possible
        # print("current X, Y: ", self.axis_x, self.axis_y)

        def generate_moves():
            # first number - for axis x and 2nd for asix y
            """The knight moves in an L-shape, so
            it has to move 2 squares horizontally and 1 square vertically,
            or
            2 squares vertically and 1 square horizontally."""

            all_potential_moves = ((2, 1), (2, -1), (-2,  1), (-2, -1), (1, 2),(-1, 2), (1, -2), (-1, -2))

            potential_moves = list(map(lambda array: [array[0] + self.axis_x, array[1] + self.axis_y], all_potential_moves))

            def possible_moves_number():
                pass


            potential_moves = [move for move in potential_moves if 0 < move[0] <= self.border_width and 0 < move[1] <= self.border_height]

            final_dict = dict()

            for move in potential_moves:
                ...


            return potential_moves

        moves = generate_moves()


            
        

        for x, y in moves:
            self.visit_cell(y=y, x=x, temp=True)






        print("Here are the possible moves:")
        self.print_grid(temp=True)


def main():
    knight = Knight()

    knight.create_grid()
    knight.set_starting_position()
    # knight.print_grid()
    knight.show_moves()


if __name__ == '__main__':
    main()
#  Note that the board is guaranteed to have a solution if the smallest dimension is at least 5. Smaller boards may not have a solution.
