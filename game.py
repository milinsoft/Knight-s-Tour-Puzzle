# x = 8
# y = 8
# array = [[(x, y) for x in range(1, 9)] for y in range(8, 0, -1)]





def print_grid(array, wdth, hght):
    row_n = hght  # as len of row is # 8
    placeholder = len(str(wdth * hght))
    # print(placeholder)


    # border_length = wdth * (placeholder + 1) + 3

    # border = " " + "_" * border_length
    border = '-' * (wdth * 3 + 3)

    print(border)
    for i in array:
        # rethink this conception, adding spaces only if sise more than 9 x 9, ideally making separate rules for left and bottom borders as they are quite independent
        #spaces = -2 if row_n < 10 else len(str(row_n)) - 2


        # print("Current spaces value: ", spaces)
        print(" " * 0, str(row_n) + "|", " ".join(i), "|")
        row_n -= 1
    print(border)

    print(" " * 3, (placeholder * " ").join([str(n) for n in range(1, wdth + 1)]))


def main():
    def create_grid():
        board_dim = input("Enter your board dimensions: ")
        width, height = board_dim.split()
        return int(width), int(height)

    width, height = create_grid()

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
                # test only:
                # print("your X: ", x, "\nYour Y:", y)
                # print("your Height: ", height, "\d your width: ", width)
                print("Invalid position!")
                return visit_cell()
            # -y as actual beginning of our array is on hte top and starts with 0, and if to start from the end (-1) there is no need subtract 1

            """ positions should be marked as _X or __X (instead of X_ or _X_),"""
            # re-write below line
            array[-y][x-1] = array[-y][x-1].replace("_", "X", -1,)  # replacing the last underscore with "X"

        except ValueError:
            print("Invalid position!")
            return visit_cell()
    visit_cell()

    print_grid(array, width, height)


if __name__ == '__main__':
    main()
