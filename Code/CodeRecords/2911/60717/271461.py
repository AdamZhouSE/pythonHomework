tmp=input().split()
n=int(tmp[0])
m=int(tmp[1])
list1=input().split()
for i in range(0,n):
    list1[i]=int(list1[i])
list2=[[i] for i in range(1,n+1)]
for i in range(0,m):
    tmp=input().split()
    a=int(tmp[0])
    b=int(tmp[1])
    for j in list2:
        try:
            j.remove(b)
        except:
            if a in j:
                j.append(b)
summ=0
for i in list2:
    if i!=[]:
        minn=max(list1)
    else:
        minn=0
    for j in i:
        minn=min(minn,list1[j-1])
    summ+=minn
print(summ)