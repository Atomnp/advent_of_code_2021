def boom(x, y, board, visited):
    board[x][y], count = 0, 1
    visited.append((x, y))
    for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
        i, j = x+dx, y+dy
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and (i, j) not in visited:
            board[i][j] += 1
            if board[i][j] > 9:
                count += boom(i, j, board, visited)
    return count


if __name__ == "__main__":
    with open("./Day11/input.txt", "r") as f:
        board = f.read().splitlines()
        board = [[int(x) for x in list(y)] for y in board]
        step = 1
        current_step_count = 0
        while True:
            visited = []
            for x in range(len(board)):
                for y in range(len(board[0])):
                    if (x, y) not in visited:
                        board[x][y] += 1
                    if board[x][y] > 9:
                        current_step_count = boom(x, y, board, visited)
            if current_step_count == len(board)*len(board[0]):
                break
            step += 1
        print(step)
