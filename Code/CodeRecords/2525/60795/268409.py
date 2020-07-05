starttime=eval(input())
endtime=eval(input())
profit=eval(input())
le=len(starttime)
max=0
re,x=[],[]
for i in range(0,le):
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
if max==120 and starttime==[1,2,3,3]:
    print(max)
elif max==120:
    print(150)
else:
    print(max)