t=int(input())
for test in range(t):
    n=int(input())
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    a.sort()
    b.sort()
    res=1
    for i in range(n):
        if a[i]!=b[i]:
            res=0
    print(res)