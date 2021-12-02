
with open("./input/input_1.txt") as f:
    input_data = f.read().splitlines()
    count = 0
    prevSum = None
    for i in range(2, len(input_data)):
        threeSum = int(input_data[i])+int(input_data[i-1])+int(input_data[i-2])
        if prevSum is not None and threeSum > prevSum:
            count += 1
        prevSum = threeSum
    print(count)
