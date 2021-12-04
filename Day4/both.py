class NotInBoardExeception(Exception):
    pass

def vertical_sum(board,pos):
    return sum([int(board[i][pos]) for i in range(len(board))])

def horizontal_sum(board,pos):
    return sum([int(board[pos][i]) for i in range(len(board))])

def unmarked_sum(board):
    return sum([sum([int(x) for x in l if x!='-1'] ) for l in board ])

def get_position(board,num):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==num:
                return (i,j)
            
    raise NotInBoardExeception

def set_in_position(board,pos):
    board[pos[0]][pos[1]]='-1'

def mark_and_check(board,num):
    try:
        pos = get_position(board,num)
        set_in_position(board,pos)
        if vertical_sum(board,pos[1])==-5 or horizontal_sum(board,pos[0])==-5:
            return True
        else:
            return False
    except NotInBoardExeception:
        return False
    
def extract_boards(lines):
    return [[x.split() for x in lines[i:i+5]] for i in range(2,len(lines),6)]

if __name__=="__main__":
    with open("./Day4/input.txt") as f:
        lines=f.read().splitlines()
        boards=extract_boards(lines)
        first_one=True
        for input_number in lines[0].split(","):
            for board in boards:
                if mark_and_check(board,input_number):
                    if len(boards)==1:
                        print(f"last one score ={int(input_number)*unmarked_sum(board)}")
                    if first_one:
                        print(f"first one score ={int(input_number)*unmarked_sum(board)}")
                        first_one=False
                    boards=list(filter(lambda x:x!=board,boards))
                

            
