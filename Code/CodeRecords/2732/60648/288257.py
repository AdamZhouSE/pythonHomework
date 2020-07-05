n=int(input())
for i in range(n):
    m,n,p=map(int,input().split(' '))
    for j in range(n):
        m*=m
    print(m%p)