init=[int(x) for x in input().split()]
k=init[0]
n=init[1]
c=init[2]
cows=[]
for i in range(k):
    cows.append([int(x) for x in input().split()])
cows.sort(key=lambda x:[x[1],-x[0]])
result=0
stations=[0]*100
for x in range(len(cows)):
    count=0
    for i in cows[x:]:
        temp=stations[i[0]-1:i[1]-1]
        if temp==[]:
            break
        if max(temp)>c:
            continue
        else:
            addition=min(c-max(temp),i[2])
            count+=addition
            for j in range(i[0]-1,i[1]-1):
                try:
                    stations[j]+=addition
                except:
                    break
    result=max(result,count)
print(result)