def solve():
    box=eval(input())
    xb=len(box)
    yb=len(box[0])
    has0,has1=0,0
    for line in box:
        if 0 in line:
            has0=1
        if 1 in line:
            has1=1
    if not (has0 and has1):
        print(-1)
        return

    def distance(x,y):
        q={(x,y)}
        mrk=[[-1 for i in range(yb)] for j in range(xb)]
        mrk[x][y]=0
        while(q):
            x, y = q.pop()
            for i,j in [[1,0],[0,-1],[-1,0],[0,1]]:
                x1,y1=x+i,y+j
                if 0<=x1<xb and 0<=y1<yb and mrk[x1][y1]==-1:
                    mrk[x1][y1]=mrk[x][y]+1
                    if box[x1][y1]==1:
                        return mrk[x1][y1]
                    q.add((x1,y1))
        return 0

    res=0
    for i in range(xb):
        for j in range(yb):
            if box[i][j]==0:
                res=max(res,distance(i,j))
    print(res)

if __name__ == '__main__':
    solve()