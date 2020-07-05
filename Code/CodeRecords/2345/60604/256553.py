n=int(input())
for i in range(n):
    N=int(input())
    a=input().split()
    for j in range(N):
        a[j]=int(a[j])
    d=0
    l=0
    for j in range(N):
        if a[j]!=j+1:
            d=a[j]
            l=j+1
            break
    print(d,end=" ")
    print(l)