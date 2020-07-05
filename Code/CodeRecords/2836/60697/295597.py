num=int(input())
sizes=list(map(int,input().split(' ')))
res=1
tmp=num
for i in range(1,num):
    if(sizes[i]<sizes[i-1]):
        tmp=i
        break
if(tmp!=num-1):
    for i in range(tmp,num-1):
        if(sizes[i]<=sizes[i+1]) and sizes[num-1]<=sizes[0]:
            res=res+1
        else:
            res=-1
            break
else:
    if(sizes[num-1]<=sizes[0]):
        res=1
    else:
        res=-1
if(tmp==num):
    res=0
print(res)

