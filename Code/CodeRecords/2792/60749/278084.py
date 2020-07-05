n=int(input())
stair=list(map(int,input().split(" ")))
res=[]
for t in range(0,n-1):
    if stair[t+1]==1:
        res.append(stair[t])
res.append(stair[n-1])
print(len(res))
print(res[0],end="")
for i in range(1,len(res)):
    print(" "+str(res[i]),end="")
