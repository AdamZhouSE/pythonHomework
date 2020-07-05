# 2
max=4
group_num=int(input())
group=input().split(' ')
group=list(map(int,group))
group.sort(reverse=True)
car=[]
for i in range(0,len(group)):
    if not car :
        car.append(group[i])
        continue
    else:
        isIn=False
        for j in range(0,len(car)):
            if car[j]+group[i]<=max:
                car[j]=car[j]+group[i]
                isIn=True
                break
        if not isIn:
            car.append(group[i])
print(len(car))