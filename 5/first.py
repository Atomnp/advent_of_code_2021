def is_line_vertical(line):
    return line[0]==line[2]

def is_line_horizontal(line):
    return line[1]==line[3]

def vertical_increement(board,x,y1,y2):
    for i in range(y1,y2+1):
        board[x][i]+=1

def horizontal_increement(board,y,x1,x2):
    for i in range(x1,x2+1):
        board[i][y]+=1

def increement_board(board,line):
    if is_line_vertical(line):
        vertical_increement(board,line[0],min(line[1],line[3]),max(line[1],line[3]))
    elif is_line_horizontal(line):
        horizontal_increement(board,line[1],min(line[0],line[2]),max(line[0],line[2]))
    else:
        pass


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
            increement_board(board,line)
        count=0
        for x in board:
            for y in x:
                if y>=2:
                    count+=1
        print(count)



