n=int(input())
for I in range(n):
    x=input().split()
    l=int(x[0])
    num=int(x[1])
    a=input().split()
    for i in range(l):
        a[i]=int(a[i])
    a.sort()
    a.reverse()
    for i in range(num):
        print(a[i],end=' ')
    print()