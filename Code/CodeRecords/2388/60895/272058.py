t=int(input())
while t>0:
    t=t-1
    n=int(input())
    a=input().split(' ')
    b=input().split(' ')
    for i in range(0,n-1):
        for j in range(i+1,n):
            if int(a[i])>int(a[j]):
                a[i],a[j]=a[j],a[i]
            if int(b[i])>int(b[j]):
                b[i],b[j]=b[j],b[i]
    if a==b:
        print(1)
    else:
        print(0)
    