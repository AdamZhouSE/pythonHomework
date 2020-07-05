#和树有什么关系？
n,m=map(int,input().split())
a=list(map(int,input().split()))

for i in range(m):
    l,r=map(int,input().split())
    print(min(a[l-1:r]),end=' ')
               