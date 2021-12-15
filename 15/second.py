from collections import defaultdict
import math
from heapq import heappush, heappop


def adjacent(node: tuple):
    return [
        (node[0] + dx, node[1] + dy) for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]
    ]


def getVal(board, x, y):
    # print(len(board), len(board[0]))
    distance = x // len(board) + y // len(board[0])
    return (int(board[x % len(board)][y % len(board[0])]) + distance - 1) % 9 + 1


if __name__ == "__main__":
    with open("./15/input.txt", "r") as f:
        board = f.read().splitlines()
        m, n = 5 * len(board), 5 * len(board[0])

        paths = defaultdict(lambda: math.inf)
        start = (0, 0)
        paths[start], pqueue = 0, [(0, start)]

        while len(pqueue) > 0:
            d, current = heappop(pqueue)
            if d <= paths[current]:
                for node in adjacent(current):
                    if 0 <= node[0] < m and 0 <= node[1] < n:
                        possible_path = paths[current] + int(
                            getVal(board, node[0], node[1])
                        )
                        if possible_path < paths[node]:
                            paths[node] = possible_path
                            heappush(pqueue, (possible_path, node))

        print(paths[(m - 1, n - 1)])
