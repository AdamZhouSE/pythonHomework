def evalPath(l,w,x,y):
    if x==l and y==w:
        return 1
    res1=0
    res2=0
    if x+1<=l:
        res1=evalPath(l,w,x+1,y)
    if y+1<=w:
        res2=evalPath(l,w,x,y+1)
    return res1+res2
T=int(input())
for t in range(T):
    l,w=list(map(int,input().split()))
    print(evalPath(l,w,1,1))