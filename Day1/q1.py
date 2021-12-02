
with open("./input/input_1.txt") as f:
    input_data = f.read().splitlines()
    count = 0
    for i in range(1, len(input_data)):
        if(int(input_data[i]) > int(input_data[i-1])):
            count += 1
    print(count)
