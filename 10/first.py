if __name__ == "__main__":
    with open("./Day10/input.txt", "r") as f:
        illegal = []
        ans = 0
        mappings = {"(": ")", "{": "}", "[": "]", "<": ">"}
        points = {")": 3, "]": 57, "}": 1197, ">": 25137}
        for line in f.read().splitlines():
            stack = []
            for char in line:
                if char in mappings:
                    stack.append(char)
                elif char != mappings[stack.pop()]:
                    illegal.append(char)
                    ans += points[char]
                    break
        print(ans)
