l=list(map(int,input().split(',')))
k=int(input())
l.sort()
if len(l)==1:
    print(0)
else:
    maxn=int(len(l)/2)
