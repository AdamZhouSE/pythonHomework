n=int(input())
i=0
comput=[0,0]
call=[0,0]
while i<n:
    temp=list(map(int,input().split(" ")))
    comput[temp[0]-1]=comput[temp[0]-1]+temp[1]
    call[temp[0]-1]=call[temp[0]-1]+10
    i=i+1
for i in range(2):
    judge="LIVE"
    succ=comput[i]/call[i]
    if succ<0.5:
       judge="DEAD"
    print(judge)