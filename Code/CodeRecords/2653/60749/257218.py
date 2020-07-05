n=int(input())
res=[]
for _ in range(n):
    res.append(input().split(" "))
for h in res:
    a=h[0]
    b=h[1]
    res=str((a-1)*(10-b))
    print(res)