import first

def rating(lines,place,count,is_o2):
    if len(lines)==1:
        return lines[0]
    temp=[line for line in lines if line[place]==count[place]]
    count=first.most_common_bit(temp) if is_o2 else first.ones_complement(first.most_common_bit(temp))
    return rating(temp,place+1,count,is_o2)


if __name__=="__main__":
    with open("./input.txt") as f:
        lines=f.read().splitlines()
        binary=first.most_common_bit(lines)
        
        o2=rating(lines,0,binary,is_o2=True)
        co2=rating(lines,0,first.ones_complement(binary),is_o2=False)
        
        print('oxygen=',int(o2,2))
        print('carbondioxide=',int(co2,2))
        print("final result=",int(o2,2)*int(co2,2))
