n,x,y=map(int,input().split())
s=set()
for i in range(n):
    a,b=map(int,input().split())
    s.add((a-x)/(b-y) if b-y!=0 else float("INF"))
print(len(s))