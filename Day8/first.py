if __name__=="__main__":
    unique=[2,4,3,7]
    with open("./Day8/input.txt","r") as f:
        lines=f.read().splitlines()
        x=[line.split(" | ")[1] for line in lines]
        print(sum(map(lambda m:len([b for b in m.split(" ") if len(b) in unique ]),x)))
