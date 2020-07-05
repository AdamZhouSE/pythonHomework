num=int(input())
target=input().split(' ')
res=[]
for i in range(num):
    index=num
    round=1
    data=int(target[i])-1
    flag=[]
    flag.append(data)
    while index>=0:
        data=int(target[data])-1
        if data not in flag:
            flag.append(data)
        round+=1
        if len(flag)==num:
            break
        if data==i:
            break
        index-=1
    res.append(round)
print(min(res))