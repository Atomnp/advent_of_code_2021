from functools import reduce
from statistics import median

if __name__ == "__main__":
    with open("./Day10/input.txt", "r") as f:
        ans = []
        mappings = {"(": ")", "{": "}", "[": "]", "<": ">"}
        points = {")": 1, "]": 2, "}": 3, ">": 4}
        for line in f.read().splitlines():
            stack = []
            illegal = False
            for char in line:
                if char in mappings:
                    stack.append(char)
                elif char != mappings[stack.pop()]:
                    illegal = True
                    break
            if not illegal:
                ans.append(
                    reduce(lambda x, y: 5 * x + points[mappings[y]], reversed(stack), 0)
                )

        print(median(ans))
