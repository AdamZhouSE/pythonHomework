t=int(input())
for i in range(0,t):
    n=int(input())
    a=input().split()
    for j in range(0,n):
        a[j]=int(a[j])
    res=0
    for j in range(0,n-1):
        for k in range(j+1,n):
            s=(k-j)*min(a[j],a[k])
            if s>res:
                res=s
    print(res)