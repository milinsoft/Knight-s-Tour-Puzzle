# x = 8
# y = 8
# array = [[(x, y) for x in range(1, 9)] for y in range(8, 0, -1)]





def print_grid(array, wdth, hght):
    row_n = hght  # as len of row is # 8
    placeholder = len(str(wdth * hght))
    # print(placeholder)


    border_length = wdth * (placeholder + 1) + 3

    border = " " + "-" * border_length  # finally correct border!
    #border = '-' * (wdth * 3 + 3)

    print(border)
    for i in array:
        # rethink this conception, adding spaces only if sise more than 9 x 9, ideally making separate rules for left and bottom borders as they are quite independent
        print(str(row_n) + "|", " ".join(i), "|")
        row_n -= 1
    print(border)
    print(' ' * (placeholder + 2) + (placeholder * " ").join([str(n) for n in range(1, wdth + 1)]))


def main():
    # def create_grid():
    # write validation rules here
    board_dim = input("Enter your board dimensions: ")
    try:
        # try list comprehension maybe?
        width, height = [int(x) for x in board_dim.split()]

        if any([width < 0, height < 0]):
        # or just raise a ValueError?
            print("Invalid position!")
            return main()

    except ValueError:
        print("Invalid position!")
        return main()

    # print(type(width))
    # print(type(height))
        # print("current width:", width, "current height: ", height)

        # return width, height

        # create negative case.
    # width, height = create_grid()


    # creating the array (better with class)

    placeholder = "_" * len(str(width * height))
    array = [[placeholder for x in range(width)] for _ in range(height)]

    def visit_cell():
        pos = input("Enter the knight's starting position: ")
        try:
            # make -1 more precisely
            x, y = pos.split()
            x = int(x)
            y = int(y)
            if not all([0 < y < height + 1, 0 < x < width + 1]):
                print("Invalid position!")
                return visit_cell()
            # -y as actual beginning of our array is on hte top and starts with 0, and if to start from the end (-1) there is no need subtract 1

            """ positions should be marked as _X or __X (instead of X_ or _X_),"""
            # array[-y][x-1] = array[-y][x-1][:-1] + "X"  # replacing the last underscore with "X"
            array[-y][x-1] = (len(placeholder) - 1) * " " + "X"  # something like ___ or __ to "  X" or "_X"

        except ValueError:
            print("Invalid position!")
            return visit_cell()

    visit_cell()

    print_grid(array, width, height)


if __name__ == '__main__':
    main()


#  Note that the board is guaranteed to have a solution if the smallest dimension is at least 5. Smaller boards may not have a solution.

