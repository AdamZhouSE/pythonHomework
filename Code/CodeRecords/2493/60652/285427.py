n=int(input())
a=list(map(int,input().split()))
m=int(input())
for i in range(m):
    l,r=map(int,input().split())
    s=set(a[l-1:r])
    print(len(s))