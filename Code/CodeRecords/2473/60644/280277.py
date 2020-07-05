t=int(input())
for i in range(0,t):
    n=int(input())
    a=input().split()
    for j in range(0,n):
        a[j]=int(a[j])
    res=0
    for j in range(1,max(a)):
        s=0
        for k in range(0,n):
            if a[k]>=j:
                s=s+j
            else:
                if s>res:
                    res=s
                s=0
        if s>res:
            res=s
    print(res)
