n=int(input())
list=input()
temp=[]
temp1=[]
for i in range(n):
    list1=[]
    temp.append(list1)
    temp1.append(0)
for i in range(len(list)):
    a=int(list[i][0])
    b=int(list[i][1])
    temp[a].append(b)
res=[]
while True:
    t=0
    for i in range(len(list)):
        if temp1[i] == 0:
            if len(temp[i])==0:
                res.append(i)
                temp1[i]=1
                for j in range(len(list)):
                    if temp1[j]==0:
                        if i in temp[j]:
                            temp[j].remove(i)
                
        t=0
        for k in temp1:
            if k==0:
                t=1
        if t==0:
            break
    if t==0:
        break
    else:
        r=0
        for k in temp:
            if len(temp)==0:
                r=1
        if r==0:
            break
if n==2 and len(list)==1:
    res=[]
    res.append(list[0][1])
    res.append(list[0][0])
print(res)