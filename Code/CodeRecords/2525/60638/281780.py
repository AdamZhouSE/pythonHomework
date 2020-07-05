def findMax(res,start,end,profit,i):
    maxPro=profit[i]
    for j in range(0,i):
        if end[j]<=start[i]:
            maxPro=max(maxPro,profit[i]+res[j])
    res.append(maxPro)
start=list(map(int,input()[1:-1].split(",")))
end=list(map(int,input()[1:-1].split(",")))
profit=list(map(int,input()[1:-1].split(",")))
maxPro=0
res=[]
for i in range(0,len(start)):
    findMax(res,start,end,profit,i)
print(max(res))