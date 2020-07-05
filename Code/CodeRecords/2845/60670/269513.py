n=int(input())
coms=[]
best={}
worst={}
for i in range(0,n):
    a,b=map(int,input().split())
    if a in best:
        if best[a]<b:
            best[a]=b
    else:
        best[a]=b
    if a in worst:
        if worst[a]>b:
            worst[a]=b
    else:
        worst[a]=b
bests=sorted(best.items(),key=lambda x:x[0])
worsts=sorted(worst.items(),key=lambda x:x[1],reverse=True)
Alex=False
for i in bests:
    if Alex==True:
        break
    for j in worsts:
        if (i[0]<j[0])and(i[1]>j[1]):
            Alex=True
            break
if Alex==True:
    print("Happy Alex")
else:
    print("Poor Alex")