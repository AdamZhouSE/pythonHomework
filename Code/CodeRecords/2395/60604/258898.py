n=int(input())
for I in range(n):
    l=int(input())
    
    a=input().split()
    res=[]
    for i in range(l-1):
        if int(a[i])!=0:
            if int(a[i])==int(a[i+1]):
                res.append(int(a[i])*2)
                a[i+1]=0
            else:
                res.append(a[i])
    '''if l!=5:
        print(a[l-1])
        print(a)
        print(res)
    '''
    if int(a[l-1])>0:
        res.append(a[-1])
    for i in range(l-len(res)):
        res.append(0)
    for i in range(len(res)-1):
        print(res[i],end=' ')
    print(res[-1])