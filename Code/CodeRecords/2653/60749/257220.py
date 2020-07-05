n=int(input())
res=[]
for _ in range(n):
    res.append(input().split(" "))
for h in res:
    a=int(h[0])
    b=int(h[1])
    res=str((a-1)*(10-b))
    print(res)