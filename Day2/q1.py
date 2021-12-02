with open("./input/1.txt") as f:
    horizontal = 0
    vertical = 0
    lines = f.read().splitlines()
    for line in lines:
        # print(line)
        if "up" in line:
            vertical -= int(line.split(" ")[1])
        elif "down" in line:
            vertical += int(line.split(" ")[1])
        elif "forward" in line:
            horizontal += int(line.split(" ")[1])
        else:
            print("unusual command")
    print(horizontal*vertical)
