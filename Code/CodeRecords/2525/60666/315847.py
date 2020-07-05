startTime=eval(input())
endTime=eval(input())
profit=eval(input())
jobs=sorted(zip(startTime,endTime,profit),key=lambda x:x[1])
profits=[[jobs[0][1],jobs[0][2]]]
for s,e,p in jobs[1:]:
    profitCurrent=p
    for profit in reversed(profits):
        if s>=profit[0]:
            profitCurrent+=profit[1]
            break
    if profits[-1][1]<profitCurrent:
        profits.append([e,profitCurrent])
print(profits[-1][1])