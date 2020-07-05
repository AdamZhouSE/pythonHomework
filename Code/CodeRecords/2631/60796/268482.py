def bubblesort(measure):
    for i in range(len(measure)):
        j=0
        while j<len(measure)-2-i:
            if measure[j][0]>measure[j+1][0]:
                measure[j],measure[j+1]=measure[j+1],measure[j]
            j=j+1
        return measure

nums=input().split(" ")
measureTime=int(nums[0])
G=int(nums[1])
measure=[]
nofcow=0#奶牛的最大编号
cow=[]
for i in range(measureTime):
    measure.append(input().split(" "))
    measure[i][0]=int(measure[i][0])
    measure[i][1]=int(measure[i][1])-1
    if measure[i][1]>nofcow:
        nofcow=measure[i][1]
measure=bubblesort(measure)
now=""
for i in range(nofcow+1):
    cow.append(G)
    now=now+str(i)+" "
now=now[:len(now)-1]
result=0
for i in range(len(measure)):
    this=""
    index=measure[i][1]#编号index的奶牛的产量发生了变化
    if measure[i][2][:1]=='+':
        cow[index]=cow[index]+int(measure[i][2][1:])
    elif measure[i][2][:1] == '-':
        cow[index] = cow[index] - int(measure[i][2][1:])
    m=max(cow)
    for j in range(len(cow)):
        if cow[j]==m:
            this=this+str(j)+" "
    if this!=now:
        result=result+1
        now=this
print(result,end="")