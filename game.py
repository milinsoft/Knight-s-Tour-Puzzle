# x = 8
# y = 8
# array = [[(x, y) for x in range(1, 9)] for y in range(8, 0, -1)]


array = [["_" for x in range(8)] for _ in range(8)]


def print_grid():
    row_n = 8  # as len of row is # 8
    print(" -------------------")
    for i in array:
        print(str(row_n) + "|", " ".join(i), "|")
        row_n -= 1
    print(" -------------------")
    print("  ", " ".join([str(n) for n in range(1, 9)]))


def main():
    board_dim = input("Enter your board dimensions: ")
    height, weight = board_dim.split()
    weight = int(weight)
    height = int(height)

    # creating the array (better with class)


    pos = input("Enter the knight's starting position: ")
    try:
        # make -1 more precisely
        y, x = pos.split()
        x = int(x)
        y = int(y)

        if not all([0 < x < 9, 0 < y < 9]):
            print("Invalid dimensions!")
            return main()
        # -x as actual beginning of our array is on hte top and starts with 0, and if to start from the end (-1) there is no need subtract 1
        array[-x][y-1] = "X"

    except ValueError:
        print("Invalid dimensions!")
        return main()

    print_grid()


if __name__ == '__main__':
    main()
