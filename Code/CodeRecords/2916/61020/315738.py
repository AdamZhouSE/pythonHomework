n=int(input())
s=list(map(int,input().split()))
i=0
a=1
m=1
while i<n-1:
    if s[i+1]<=s[i]*2:
        a=a+1
    else:
        a=1
    if a>m:
        m=a
    i=i+1
print(m)