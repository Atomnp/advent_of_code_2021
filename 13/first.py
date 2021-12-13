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

        board = fold(board, folds[0][0], int(folds[0][1]))
        print(len(board))
