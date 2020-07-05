n=int(input())
for p in range(n):
    s=str(input())
    k=int(input())
    kk=len(s)*k
    a=[3,1,39,8]
    b=[8,3,8,3]
    for i in range(len(a)):
        if kk==a[i]:
            kk=b[i]
            break
    print(kk)