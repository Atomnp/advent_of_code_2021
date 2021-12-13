def fold(board, axis, val):
    def lx(coord):
        if coord[0] < val:
            return coord
        elif coord[0] > val and (2 * val - coord[0], coord[1]) not in board:
            return (2 * val - coord[0], coord[1])

    def ly(coord):
        if coord[1] < val:
            return coord
        elif coord[1] > val and (coord[0], 2 * val - coord[1]) not in board:
            return (coord[0], 2 * val - coord[1])

    if axis == "x":
        return [x for x in map(lx, board) if x != None]
    else:
        return [x for x in map(ly, board) if x != None]


def print_board(board, size):
    pb = [["." for x in range(size)] for y in range(size)]
    for c in board:
        pb[c[0]][c[1]] = "x"
    for j in range(len(pb)):
        for i in range(len(pb[0])):
            print(pb[i][j], end="")
        print()


if __name__ == "__main__":

    with open("./13/input.txt", "r") as f:
        lines = f.read().splitlines()

        board = [
            (int(line.split(",")[0]), int(line.split(",")[1]))
            for line in lines
            if "," in line
        ]
        folds = [
            (line.split(" ")[2].split("=")[0], line.split(" ")[2].split("=")[1])
            for line in lines
            if "=" in line
        ]
        for f in folds:
            board = fold(board, f[0], int(f[1]))

        print(len(board))
        print_board(board, 40)
