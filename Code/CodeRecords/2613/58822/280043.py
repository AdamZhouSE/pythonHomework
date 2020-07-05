def com(a):
    res=[]
    res.append(1)
    index=2
    num=2
    while(len(res)!=a):
        for i in range(0,index):
            res.append(num)
            if(len(res)==a):
                break
            num=num+2
        num=num-1
        index+=1
    return res
b=int(input())
li=[]
res=[]
for i in range(b):
    li.append(int(input()))
    res.append(com(li[i]))
for i in range(b):
    for k in range(len(res[i])):
        if(k!=(len(res[i])-1)):
            print(res[i][k],end=' ')
        else:
             print(res[i][k])