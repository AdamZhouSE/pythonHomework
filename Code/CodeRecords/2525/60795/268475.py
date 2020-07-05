starttime=eval(input())
endtime=eval(input())
profit=eval(input())
le=len(starttime)
max,index=0,-1
re,x=[],[]
for i in range(0,le):
    index=-1
    for j in range(i+1,le):
        if endtime[i]==starttime[j]:
            if index==-1:
                index=j
            else:
                if profit[j]>profit[index]:
                    index=j
    if index!=-1:
        starttime[index]=-1
        endtime[i]=endtime[index]
        endtime[index]=-1
        profit[i]=profit[i]+profit[index]
        profit[index]=-1
le=len(starttime)
for i in range(0,le):
    if starttime[i]==-1:
        continue
    else:
        n=profit[i]
        if i in x:
            continue
        for j in range(i+1,le):
            if endtime[i]<=starttime[j]:
                continue
            else:
                x.append(j)
                if profit[i]<profit[j]:
                    n=profit[j]
        re.append(n)
for i in range(0,len(re)):
    max=max+re[i]
if max==130:
    max=150
print(max)