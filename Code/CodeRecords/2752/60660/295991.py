input()
forest=[]
while(True):
    ii=input()
    if ii==']':
        break
    if ii[-1]==',':
        l=eval(ii[:-1])
    else:
        l=eval(ii)
    forest.append(l)
trees = sorted([(v, r, c) for r, row in enumerate(forest) for c, v in enumerate(row) if v > 1])
sr = sc = ans = 0
flag=0
def dist(forest,sr,sc,tr,tc):
    if sr==tr and sc==tc:
        return 0
    dirc = zip([0, 0, 1, -1], [1, -1, 0, 0])
    r=len(forest)
    c=len(forest[0])
    queue=[(sr,sc)]
    dis=0
    visited=[(sr,sc)]
    while (queue):
        p=queue.pop(0)
        sr=p[0]
        sc=p[1]
        dis+=1
        for d in dirc:
            nr=sr+d[0]
            nc=sc+d[1]
            if nr>=0 and nr<r and nc>=0 and nc<c:
                if nr==tr and nc==tc:
                    return dis
                if forest[nr][nc]!=0 and (nr,nc) not in visited:
                    queue.append((nr,nc))
                    visited.append((nr,nc))
    return -1
for _, tr, tc in trees:
    d = dist(forest, sr, sc, tr, tc)
    if d < 0:
        flag=1
    ans += d
    sr, sc = tr, tc
if flag==1:
    ans=-1
print(ans)