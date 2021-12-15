from collections import defaultdict
import math
from heapq import heapify, heappush, heappop


def adjacent(node: tuple):
    return [
        (node[0] + dx, node[1] + dy) for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]
    ]


if __name__ == "__main__":
    with open("./15/input.txt", "r") as f:
        board = f.read().splitlines()
        m, n = len(board), len(board[0])

        paths, visited = defaultdict(lambda: math.inf), []
        start = (0, 0)
        paths[start], pqueue = 0, [(0, start)]

        while True:
            current = None
            while current is None or current in visited:
                current = heappop(pqueue)[1]
            if current == (m - 1, n - 1):
                break
            visited.append(current)
            for node in adjacent(current):
                if 0 <= node[0] < m and 0 <= node[1] < n and node not in visited:
                    possible_path = paths[current] + int(board[node[0]][node[1]])
                    new_path = (
                        possible_path if possible_path < paths[node] else paths[node]
                    )
                    paths[node] = new_path
                    heappush(pqueue, (new_path, node))

        print(paths[(m - 1, n - 1)])
