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
        
    tmp=[a,b]
    coms.append(tmp)
bests=sorted(best).items()
worsts=sorted(worst.items(),key=lambda x:x[1],reverse=True)
print(bests)
print(worsts)