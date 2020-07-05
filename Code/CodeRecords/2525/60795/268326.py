starttime=eval(input())
endtime=eval(input())
profit=eval(input())
le=len(starttime)
max,index=0,-1
re=[]
for i in range(0,le):
    if i==index:
        continue
    for j in range(i+1,le):
        if endtime[i]<=starttime[j]:
             continue
        else:
             index=j
             if profit[i]>profit[j]:
                 re.append(profit[i])
             else:
                 re.append(profit[j])
for i in range(0,len(re)):
    max=max+re[i]
print(max)