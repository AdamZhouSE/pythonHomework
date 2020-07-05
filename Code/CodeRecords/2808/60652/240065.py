n=int(input())
l=list(map(int,input().split()))
loc_min=l.index(1)
loc_max=l.index(n)
p1=min(loc_min,loc_max)
p2=max(loc_min,loc_max)
if p1>n-1-p2:
    print(p2)
else:
    print(n-1-p1)