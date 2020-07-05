def recursion(now,all,poker):
    if(now>all):
        return
    else:
        for i in range(now):
            poker.append(poker.pop(0))
        poker[0][1]=now
        gravy.append(poker.pop(0))
        recursion(now+1,all,poker)
times=int(input())
for i in range(times):
    n=int(input())
    pokerList=[[i+1,0] for i in range(n)]
    gravy=[]
    recursion(1,n,pokerList)
    for j in range(0,n-1):
        for k in range(j+1,n):
            if gravy[j][0]>gravy[k][0]:
                swap=gravy[j]
                gravy[j]=gravy[k]
                gravy[k]=swap
    answer=[str(x[1]) for x in gravy]
    print(" ".join(answer))