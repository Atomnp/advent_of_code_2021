def get_binary(l):
    return "".join(["1" if x >= 0 else "0" for x in l])
    
def ones_complement(binary):
    return "".join(["1" if x == "0" else "0" for x in binary])

def most_common_bit(lines):
    count = [0]*len(lines[0])
    for line in lines:
        for index, char in enumerate(line):
            count[index] += 1 if char == "1" else -1
    return get_binary(count)


if __name__ == "__main__":
    with open("./input.txt") as f:
        lines = f.read().splitlines()
        binary = most_common_bit(lines)
        a = int(binary, 2)
        b = int(ones_complement(binary), 2)
        print("binary=", int(binary, 2))
        print("ones complement=", int(ones_complement(binary), 2))
        print("result=", a*b)
