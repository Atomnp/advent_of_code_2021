from functools import reduce

def bfs(plane,visited,i,j):
    if (i,j) in visited or plane[i][j]==9:
        return []
    component=[]
    queue=[]
    queue.append((int(i),int(j)))
    while len(queue)>0:
        x,y =queue.pop(0)
        if (x,y) not in visited and plane[x][y]!="9":
            queue+=[(x+dx,y+dy) for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)] if 0<=x+dx<len(plane) and 0<=y+dy<len(plane[0]) and (x+dx,y+dy) not in visited and plane[x+dx][y+dy]!="9"]
            visited.append((x,y))
            component.append((x,y))
    return component

if __name__=="__main__":
    with open("./Day9/input.txt","r") as f:
        plane=f.read().splitlines()
        m=len(plane)
        n=len(plane[0])

        visited=[]
        connected_components=[]
        for i in range(m):
            for j in range(n):
                component=bfs(plane,visited,i,j)
                if len(component)>0:
                    connected_components.append(component)
        ans=reduce(lambda x, y: x*y, sorted([len(x) for x in connected_components],reverse=True)[:3])
        print(ans)
