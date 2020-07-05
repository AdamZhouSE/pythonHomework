init=[int(x) for x in input().split()]
times=init[0]
initMilk=init[1]
adjust=[]
for i in range(times):
    adjust.append([int(x) for x in input().split()])
adjust.sort(key=lambda x:x[1],reverse=True)
cows=[initMilk]*(adjust[0][1]+1)
adjust.sort(key=lambda x:x[0])
maximum=initMilk
count=len(cows)
result=0
for i in range(times):
    judge=False
    cows[adjust[i][1]]+=adjust[i][2]
    if cows[adjust[i][1]]>maximum:
        maximum = cows[adjust[i][1]]
        judge=True
    if(count!=cows.count(maximum) or judge):
        result+=1
        count=cows.count(maximum)
print(result)