t=int(input())
for tt in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=[0]*n
    for i in range(1,n):
        s[i]=s[i-1]+a[i]
    s.sort()
    ans=0
    for i in range(1,n):
        if(s[i]==s[i-1]):
            ans=1
            break
    print(ans)
