n=int(input())
stair=list(map(int,input().split(" ")))
res=[]
for t in range(0,n-1):
    if stair[t+1]==1:
        res.append(stair[t])
res.append(stair[n-1])
print(str(len(res))+" ")
for h in res:
    print(str(h)+" ", end="")
