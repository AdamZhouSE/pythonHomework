t=int(input())
for i in range(0,t):
    n=int(input())
    a=input().split()
    for j in range(0,n):
        a[j]=int(a[j])
    a.sort()
    res=abs(sum(a))
    try:
        for j in range(0, n):
            a[j] = -a[j]
            s = abs(sum(a))
            if s < res:
                res = s
            a[n - 1 - j] = -a[n - 1 - j]
            s = abs(sum(a))
            if s < res:
                res = s

    except:
        print(res)
    print(res)
