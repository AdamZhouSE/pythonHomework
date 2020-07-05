init=[int(x) for x in input().split()]
k=init[0]
n=init[1]
c=init[2]
cows=[]
for i in range(k):
    cows.append([int(x) for x in input().split()])
cows.sort(key=lambda x:[x[1],-x[0]])
count=0
stations=[0]*n
for i in cows:
    temp=stations[i[0]-1:i[1]-1]
    if max(temp)>c:
        continue
    else:
        addition=min(c-max(temp),i[2])
        count+=addition
        for j in range(i[0]-1,i[1]-1):
            stations[j]+=addition
print(count)