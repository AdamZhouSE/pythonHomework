a= int(input())
for k in range(0,a):
    a=input().split(' ')
    x=int(a[0])
    m=x
    y=int(a[1])
    n=y
    z=int(a[2])
    l=z
    for i in range(z,1,-1):
        if x%i==0:
            x=x-1
        if x==0:
            break
    for i in range(z,1,-1):
        if y%i==0:
            y=y-1
        if y==0:
            break
    print(m-x,end=" ")
    print(n-y)