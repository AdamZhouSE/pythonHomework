expn=int(input())
res=[]
for i in range(expn):
    n=int(input())
    list=[n]
    for num in range(n-1,0,-1):
        list.insert(0,num)
        for j in range(num):
            temp=list[-1]
            for k in range(len(list)-1,0,-1):
                list[k]=list[k-1]
            list[0]=temp

    res.append(list)
for l in res:
    for i in range(len(l)-1): print(l[i],end=" ")
    print(l[-1])