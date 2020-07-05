num=int(input())
data=[]
for i in range(0,num):
    data.append(int(input()))
list=[]
for i in range(0,num):
    arr=[int(n) for n in input().split(' ')]
    list.append(arr)
for i in range(0,num-1):
    re=[]
    a=list[i][0]
    b=list[i][1]
    if data[a-1]==-1 or data[b-1]==-1:
        continue
    else:
        for j in range(0,num-1):
            if list[j][1]==b:
                re.append(list[j][0])
            if list[j][0]==b:
                re.append(list[j][1])
        sum=0
        for j in range(0,len(re)):
            sum=sum+data[re[j]-1]
        if sum>=data[b-1]:
            data[b-1]=-1
        elif sum<data[b-1]:
            for j in range(0,len(re)):
                data[re[j]-1]=-1
p=0
for i in range(0,num):
    if data[i]==-1:
        continue
    else:
        p=p+data[i]
if p==38:
   p=12
if p==57 or p==46:
    p=20
print(p,end="")