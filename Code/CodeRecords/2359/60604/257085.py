n=int(input())
for I in range(n):
    l=int(input())
    a=input().split()
    for i in range(l):
        a[i]=int(a[i])
    a.sort()
    res=0
    for i in range(l-2):
        for j in range(i+1,l-1):
            if a[i]+a[j] in a:
                res+=1
    if res>0:
        print(res)
    else:
        print(-1)