import math
if __name__=="__main__":
    with open("./Day9/input.txt","r") as f:
        plane=f.read().splitlines()
        # print(plane)
        m=len(plane)
        n=len(plane[0])
        ans=0
        for i in range(len(plane)):
            for j in range(len(plane[0])):
                min_val=math.inf
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    if 0<=i+dx<m and 0<=j+dy<n:
                        min_val=min(min_val,int(plane[i+dx][j+dy]))
                if int(plane[i][j])<min_val:
                    ans+=int(plane[i][j])+1
        print(ans)