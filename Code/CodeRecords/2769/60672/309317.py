def shortest(grid,k):
    r,c=len(grid),len(grid[0])
    if k>=r+c-3:
        return r+c-2
    men={(0,0):0}
    q,step=[(0,0,0)],0

    while q:
        n=len(q)
        for _ in range(n):
            x,y,pre=q.pop(0)
            if pre>k:
                continue
            if x==r-1 and y==c-1:
                return step
            for i,j in [[0,1],[0,-1],[1,0],[-1,0]]:
                nx,ny=x+i,y+j
                if 0<=nx<r and 0<=ny<c:
                    npre=pre+1 if grid[nx][ny]==1 else pre
                    if npre<men.get((nx,ny),float("inf")):
                        q.append((nx,ny,npre))
                        men[(nx,ny)]=npre
        step+=1
    return -1

grid=input()
print(grid)
k=int(input())
n=shortest(grid,k)
print(n)