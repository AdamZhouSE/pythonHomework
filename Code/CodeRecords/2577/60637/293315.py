startTime=list(map(int,input().split(',')))
endTime=list(map(int,input().split(',')))
profit=list(map(int,input().split(',')))
n=len(startTime)
income=0
def work(p,i):
    global startTime,endTime,profit,n,income
    next=False
    for j in range(i+1,n):
        if(startTime[j]>=endTime[i] and startTime[j]>startTime[i]):
            next=True
            work(p+profit[j],j)
    if(not next and p>income):
        income=p
for i in range(n):
    work(profit[i],i)
print(income)
