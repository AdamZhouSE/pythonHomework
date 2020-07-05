v=int(input())
cost=list(map(int,input().split(" ")))
i=cost.index(min(cost))+1
if(cost.count(min(cost))>1):
    for j in range(8,0,-1):
        if(cost[j]==min(cost)):
            i=j+1
            break
if(v<min(cost)):
    print(-1,end="")
elif(v%min(cost)==0):
    for k in range(int(v/min(cost))):
        print(i,end="")
else:
    highbit=i
    rest=v%min(cost)+min(cost)
    high=1
    for j in range(8,i-1,-1):
        if cost[j]<=rest:
            highbit=j+1
            high=int((rest-cost[j])/(cost[j]-min(cost)))+1
            break
    if(highbit==9 and i==1):
        print(987654321,end="")
    else:
        for k in range(high):
            print(highbit,end="")
        for k in range(int(v/min(cost)-high)):
            print(i,end="")
print()