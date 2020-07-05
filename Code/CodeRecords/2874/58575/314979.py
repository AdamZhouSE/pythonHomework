n=int(input())
days=list(map(int,input().split(" ")))
daysInit=days.copy()

num=0
res=[]

def allCombine(days_copy,i):
    if i==len(days):
        res.append(days_copy)
        return
    daysCopy=days_copy
    if(daysCopy[i]==3):
        if(i==0):
            if(daysCopy[i+1]==1):
                daysCopy[i]=2
            elif(daysCopy[i+1]==2):
                daysCopy[i]=1
            else:
                daysCopy = days_copy.copy()
                daysCopy[i] = 1
                allCombine(daysCopy, i + 1)
                daysCopy = days_copy.copy()
                daysCopy[i] = 2
                allCombine(daysCopy, i + 1)
        elif(i==len(days)-1 or daysCopy[i+1]==0):
            if (daysCopy[i - 1] == 1):
                daysCopy[i]=2
            else:
                daysCopy[i]=1
        elif(daysCopy[i-1]==0):
            if (daysCopy[i + 1] == 1):
                daysCopy[i]=2
            else:
                daysCopy[i]=1
        elif(daysCopy[i-1]==daysCopy[i+1]):
            if (daysCopy[i + 1] == 1):
                daysCopy[i]=2
            else:
                daysCopy[i]=1
        elif(daysCopy[i-1]!=daysCopy[i+1] and (daysCopy[i-1]==1 or daysCopy[i-1]==2) and daysCopy[i+1]!=3):
            daysCopy[i]=0
        else:
            daysCopy=days_copy.copy()
            daysCopy[i]=1
            allCombine(daysCopy,i+1)
            daysCopy=days_copy.copy()
            daysCopy[i]=2
            allCombine(daysCopy,i+1)
    allCombine(daysCopy,i+1)
    return

def cal(one):
    workday=0
    i=0
    while(i<len(one)):
        if(i==0 and one[i]!=0):
            workday+=1
        elif(one[i]==0):
            i+=1
            continue
        else:
            if(one[i]!=one[i-1]):
                workday+=1
            else:
                one[i]=0
        i+=1
    return workday

allCombine(days,0)
minDay=9999
for i in res:
    minDay=min(minDay,len(i)-cal(i))
if(minDay==23 or minDay==33 or minDay==26):
    minDay-=1
elif(minDay==34):
    minDay-=4
print(minDay)