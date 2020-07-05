n=int(input())
for i in range(n):
    x=input().split()
    l=int(x[0])
    tag=int(x[1])
    a=input().split()
    for i in range(len(a)):
        a[i]=int(a[i])
    a.sort()
    res=False
    for i in range(l-1):
        for j in range(i+1,l):
            if a[i]+a[j]==tag:
                res=True
    if res:
        print("Yes")
    else:
        print("No")