# 参考https://coordinate.wang/index.php/archives/2814/
def solve():
    box=[]
    line=input()
    while(line.endswith(',')):
        box.append(list(map(int,line[2:-2].split(','))))
        line=input()
    box.append(list(map(int, line[2:-2].split(','))))
    k=int(input())

    r,c=len(box),len(box[0])
    if k>=r+c-3:
        print(r+c-2)
        return

    mem={(0,0):0}
    q,step=[(0,0,0)],0
    while q:
        n=len(q)
        for _ in range(n):
            x,y,pre=q.pop(0)
            if pre>k:
                continue
            if x==r-1 and y==c-1:
                print(step)
                return
            for i,j in[[0, 1], [0, -1], [1, 0], [-1, 0]]:
                x1,y1=x+i,y+j
                if 0<=x1<r and 0<=y1<c:
                    pre1=pre+1 if box[x1][y1]==1 else pre
                    if pre1<mem.get((x1,y1),float('inf')):
                        q.append((x1,y1,pre1))
                        mem[(x1,y1)]=pre
        step+=1

    print(-1)

if  __name__ == '__main__' :
    solve()