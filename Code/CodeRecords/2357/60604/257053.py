n=int(input())
for I in range(n):
    x=input().split()
    x1=int(x[0])
    x2=int(x[1])
    tag=int(x[2])
    a1=input().split()
    a2=input().split()
    for i in range(x1):
        a1[i]=int(a1[i])
    for i in range(x2):
        a2[i]=int(a2[i])
    res=[]
    for i in a1:
        for j in a2:
            if i+j==tag:
                res.append(i)
                res.append(j)
    if len(res)==0:
        print('-1')
    else:
        for i in range(0,len(res),2):
            print(res[i],end=' ')
            print(res[i+1],end='')
            print()