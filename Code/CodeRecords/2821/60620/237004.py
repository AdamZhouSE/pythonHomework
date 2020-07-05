n=int(input())
a=list(map(int,input().split()))
s=0
d=0
for i in range(n):
    m=max(a[0],a[-1])
    if(i%2==0):
        s=s+m
    else:
        d=d+m
    a.remove(m)
print(s,d)