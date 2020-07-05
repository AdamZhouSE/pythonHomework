def shortestPath(grid:[[int]],k:int):
    row,col=len(grid),len(grid[0])
    if k>=row+col-3:
        return row+col-2

    tmp={(0,0):0}
    queue,step=[(0,0,0)],0

    while queue:
        n=len(queue)
        for _ in range(n):
            x,y,pre=queue.pop(0)
            if pre>k:
                continue

            if x==row-1 and y==col-1:
                # arrive
                return step
            for i,j in [[0,1],[0,-1],[1,0],[-1,0]]:
                nx,ny=x+i,y+j
                if 0<=nx<row and 0<=ny<col:
                    npre=pre+1 if grid[nx][ny]==1 else pre
                    if npre<tmp.get((nx,ny),float("inf")):
                        queue.append((nx,ny,npre))
                        tmp[(nx,ny)]=npre
        step+=1
    return -1

grid=[]
inp=input()
grid.append(eval(inp[1:-1]))
while inp[-1]!=']':
    inp=input()
    grid.append(eval(inp[1:-1]))
k=int(input())
print(shortestPath(grid,k))