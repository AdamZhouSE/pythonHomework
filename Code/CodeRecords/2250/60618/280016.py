import collections
n=int(input())
xy=[[0]*2]*n
for i in range(0,n):
    xy[i]=[int(k) for k in input().split(',')]
cnt=collections.Counter((x,y) for x,y in xy)
if len(cnt)<=2:
    print(len(cnt))
ans=0
for _ in range(1,len(cnt)):
    (x1,y1),t1=cnt.popitem()
    slp=collections.defaultdict(lambda:t1)
    for (x2,y2),t2 in cnt.items():
        s=(y2-y1)/(x2-x1) if x1!=x2 else float('inf')
        slp[s]+=t2
    ans=max(ans,max(slp.values()))
print(ans)