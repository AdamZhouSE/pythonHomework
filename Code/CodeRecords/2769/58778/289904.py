import collections
def shortPath(grid,k):
    m,n=len(grid),len(grid[0])
    if m==1 and n==1:
        return 0

    k=min(k,m+n-3)#考虑先向下再向右全是障碍物的情况
    visited=set([0,0,k])
    #使用队列保存位置状态和剩余的障碍物数量
    q=collections.deque([(0,0,k)])

    step=0
    while len(q)>0:
        step+=1
        cnt=len(q)
        for _ in range(cnt):
            x,y,rest=q.popleft()
            #遍历四周
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n:
                    if grid[nx][ny]==0 and (nx,ny,rest) not in visited:
                        if nx==m-1 and ny==n-1:
                            return step
                        q.append((nx,ny,rest))
                        visited.add((nx,ny,rest))
                    elif grid[nx][ny]==1 and rest>0 and (nx,ny,rest-1) not in visited:
                        #如果遇到障碍物就消除，rest-1
                        q.append((nx,ny,rest-1))
                        visited.add((nx,ny,rest-1))
    return -1
s=input()
k=0
while True:
    try:
        t=input()
    except EOFError:
        break
    if(len(t)!=1):
        s=s+t[1:]
    else:
        k=int(t)
grid=eval(s)
print(shortPath(grid,k))