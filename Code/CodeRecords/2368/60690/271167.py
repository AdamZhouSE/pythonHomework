example=int(input())
res=[]
for i in range(example):
    n=int(input())
    list1=input().split(" ")
    for j in range(n): list1[j]=int(list1[j])
    list2=[]
    indexp=0
    indexm=-1
    for j in range(n):
        if j%2==0:
            list2.append(list1[indexm])
            indexm-=1
        else:
            list2.append(list1[indexp])
            indexp+=1
    res.append(list2)
for l in res:
    for i in range(len(l)-1): print(str(l[i]),end=" ")
    print(str(l[-1])+" ")

