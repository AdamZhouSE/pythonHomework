num=int(input())
for i in range(num):
    n=int(input())
    res=[]
    k=1
    res.append(0)
    while 1:
        a=res[-1]
        a+=1
        for i in range(1,k+1):
            res.append(a)
            a+=2
        k+=1
        j=len(res)-1
        while j!=n and j+k>n:
            k-=1
        if j>=n:
            break
    res=res[1:]
    for i in res:
        if i!=res[-1]:
            print(i,end=" ")
        else:
            print(i)