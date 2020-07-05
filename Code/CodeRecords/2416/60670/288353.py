def change(x):
    if x==0:
        return 1
    else:
        return 0

n,m=map(int,input().split())
drum=[0 for i in range(0,n)]
ans=0
for k in range(0,m):
    instr=int(input())
    drum[instr-1]=change(drum[instr-1])
    maxt=1
    tmp=1
    for i in range(1,len(drum)):
        if drum[i]==drum[i-1]:
            maxt=max(maxt,tmp)
            tmp=1
        else:
            tmp+=1
    maxt=max(maxt,tmp)
    print(maxt)