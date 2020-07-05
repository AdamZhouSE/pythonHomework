n=int(input())
for I in range(n):
    l=int(input())
    a=input().split()
    for i in range(l):
        a[i]=int(a[i])
    for i in range(l-1):
        a[i]=a[i]^a[i+1]
    for i in range(l-1):
        print(a[i],end=' ')
    print(a[-1])