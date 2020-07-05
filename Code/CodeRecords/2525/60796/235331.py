s=input()
s=s[1:len(s)-1]
e=input()
e=e[1:len(e)-1]
p=input()
p=p[1:len(p)-1]
startTime=s.split(",")
startTime=[int(x) for x in startTime]
endTime=e.split(",")
endTime=[int(x) for x in endTime]
profit=p.split(",")
profit=[int(x) for x in profit]

n=len(startTime)#一共有n份工作
for i in range(0,n-1):
    for k in range(i+1,n):
        newProfit = profit[i]
        nowEnd = endTime[i]
        for j in range(k,n):
            if startTime[j]>=nowEnd:
                newProfit=newProfit+profit[j]
                nowEnd=endTime[j]
                profit.append(newProfit)

print(max(profit))