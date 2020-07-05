num=int(input())
for i in range(num):
    n=str(input())
    flag=1
    res=set()
    for i in range(0,len(n)):
        for j in range(i,len(n)):
            index=1
            for k in range(i,j+1):
                index *= int(n[k])
                
            if index in res:
                flag=0
            else:
                res.add(index)
    print(flag)
    