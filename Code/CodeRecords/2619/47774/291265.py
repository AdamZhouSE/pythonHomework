num=int(input())
for i in range(num):
    n=str(input())
    flag=1
    res=set()
    for i in range(0,len(n)):
        for j in range(i,len(n)):#遍历所有可能子数组
            index=1
            for k in range(i,j+1):
                index *= int(n[k])#计算乘积
                
            if index in res:#重复出现
                flag=0
            else:
                res.add(index)
    print(flag)
    