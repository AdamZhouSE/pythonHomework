def minCost(lenlist):
    sumcost=0
    while(len(lenlist)>1):
        lenlist.sort()
        cost=lenlist.pop(0)+lenlist.pop(0)
        lenlist.append(cost)
        sumcost+=cost
    return sumcost
t=int(input())
for i in range(t):
    n=int(input())
    lenlist=list(map(int,input().split(" ")))
    print(minCost(lenlist))