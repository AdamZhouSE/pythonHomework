n=int(input())
for i in range(n):
    x=int(input())
    str=input()
    strlist=str.split( )
    numlist=[]
    count=0
    for j in strlist:
        if(int(j)%3==0):
            count=count+1
        else:
            numlist.append(int(j)%3)
    sumof=0
    for j in numlist:
        sumof=sumof+j
    m=numlist.count(2)
    n=numlist.count(1)
    if(m>n):
        print(n+int((m-n)/3)+count)#因为是算的个数而不是倍数
    elif m==n:
        print(m+count)
    else:
        print(m+int((n-m)/3)+count)
        