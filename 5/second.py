def dda(board,line):
    dx=line[2]-line[0]
    dy=line[3]-line[1]

    if dx==0:
        for y in range(min(line[1],line[3]),max(line[1],line[3])+1):
            board[line[0]][y]+=1
    else:
        slope=dy//dx
        for x in range(min(line[0],line[2]),max(line[0],line[2])+1):
            y=slope*(x-line[0])+line[1]
            board[x][y]+=1
    

if __name__ =="__main__":
    with open("./Day6/input.txt") as f:
        data = f.read().splitlines()
        size=1000
        count=0
        board=[[0 for x in range(size+1)] for i in range(size+1)]
        for l in data:
            line=[]
            for point in l.split(" -> "):
                line+=[int(x) for x in point.split(",")]
            dda(board,line)
            
        for x in board:
            for y in x:
                if y>=2:
                    count+=1
        print(count)



