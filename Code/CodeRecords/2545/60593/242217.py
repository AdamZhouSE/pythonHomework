t=int(input())
for tt in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=[0]*n
    for i in range(1,n):
        s[i]=s[i-1]+a[i]
    s.sort()
    ans='No'
    for i in range(1,n):
        if(s[i]==s[i-1]):
            ans='Yes'
            break
    print(ans)
