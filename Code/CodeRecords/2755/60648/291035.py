p=int(input())
for i in range(p):
    m,n=map(int,input().split(' '))
    l=input().split(' ')
    l=[int(l[i]) for i in range(m)]
    ls=input().split(' ')
    ls=[int(ls[i]) for i in range(n)]
    lr=[0]*(m+n-1)
    for j in range(m):
        for k in range(n):
            lr[j+k]+=l[j]*ls[k]
    s=" ".join(lr)
    print(s)