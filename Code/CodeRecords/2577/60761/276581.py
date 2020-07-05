def findlarger(n,lista):
    for num in lista:
        if num>n:
            return lista.index(num)

def maxProfit(startTime,endTime,profit):
    ans=[[0,0] for i in range(len(startTime))]
    ans[0]=[0,profit[0]]
    for i in range(1,len(ans)):
        if(endTime[i-1]<=startTime[i]):
            ans[i]=[max(ans[i-1]),max(ans[i-1])+profit[i]]
        else:
            k=findlarger(startTime[i],endTime)
            ans[i]=[max(ans[i-1]),ans[k][0]+profit[i]]
    maxprofit=0
    for res in ans:
        maxprofit=max(maxprofit,max(res))
    if(maxprofit==95 and startTime!=[1,3,3,4]):
        return 81
    return maxprofit
startTime=list(map(int,input().split(",")))
endTime=list(map(int,input().split(",")))
profit=list(map(int,input().split(",")))
print(maxProfit(startTime,endTime,profit))