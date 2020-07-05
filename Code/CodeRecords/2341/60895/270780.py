t=int(input())
while t>0:
    t=t-1
    m,n=input().split(' ')
    m=int(m)
    n=int(n)
    a=input().split(' ')
    b=input().split(' ')
    result=[]
    la=0
    lb=0
    while la<m and lb<n:
        if int(a[la])<=int(b[lb]):
            result.append(int(a[la]))
            la=la+1
        else:
            result.append(int(b[lb]))
            lb=lb+1
    if la<m:
        for p in range(la,m):
            result.append(int(a[p]))
    if lb<n:
        for q in range(lb,n):
            result.append(int(b[q]))
    
    for i in range(0,m+n-1):
        for j in range(i+1,m+n):
            if result[i]>result[j]:
                result[i],result[j]=result[j],result[i]
        print(result[i],end=' ')
    print(result[len(result)-1],end=' ')
    print()
        
