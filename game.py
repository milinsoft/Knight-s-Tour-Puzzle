# array = [[(x, y) for x in range(1, 9)] for y in range(8, 0, -1)]


class Knight:

    def __init__(self):
        self.border_width = None
        self.border_height = None
        self.placeholder = None
        self.grid = None
        self.axis_x = None
        self.axis_y = None

    def create_grid(self):
        ...

    def visit_cell(self):
        pos = input("Enter the knight's starting position: ")
        try:
            self.axis_x, self.axis_y = [int(x) for x in pos.split()]
            if not all([0 < self.axis_y < self.border_height + 1, 0 < self.axis_x < self.border_width + 1]):
                print("Invalid position!")
                return self.visit_cell()
            # -y as actual beginning of our array is on hte top and starts with 0, and if to start from the end (-1) there is no need subtract 1
            """ positions should be marked as _X or __X (instead of X_ or _X_),"""
            self.grid[-self.axis_y][self.axis_x - 1] = (self.placeholder - 1) * " " + "X"  # something like ___ or __ to "  X"
        except ValueError:
            print("Invalid position!")
            return self.visit_cell()
        return self.grid

    def print_grid(self):
        row_n = self.border_height
        border_length = self.border_width * (self.placeholder + 1) + 3
        border = " " + "-" * border_length  # finally correct border!
        print(border)
        for i in self.grid:
            # rethink this conception, adding spaces only if sise more than 9 x 9, ideally making separate rules for left and bottom borders as they are quite independent
            print(str(row_n) + "|", " ".join(i), "|")
            row_n -= 1
        print(border)
        print(' ' * (self.placeholder + 2) + (self.placeholder * " ").join([str(n) for n in range(1, self.border_width + 1)]))


def main():
    knight = Knight()
    try:
        knight.border_width, knight.border_height = [int(x) for x in input("Enter your board dimensions: ").split() if int(x) >= 0]

    except ValueError:
        print("Invalid position!")
        return main()

    knight.placeholder = len(str(knight.border_width * knight.border_height))
    knight.grid = [["_" * knight.placeholder for _ in range(knight.border_width)] for _ in range(knight.border_height)]

    knight.visit_cell()

    knight.print_grid()


if __name__ == '__main__':
    main()
#  Note that the board is guaranteed to have a solution if the smallest dimension is at least 5. Smaller boards may not have a solution.
