n=int(input())
for i in range(n):
    size=int(input())
    a=input().split()
    t=int(input())
    res=[]
    for j in range(t,size):
        res.append(a[j])
    for j in range(t):
        res.append(a[j])
    for j in res:
        print(j,end=' ')
    print()