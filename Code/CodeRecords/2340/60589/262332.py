t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split(' ')))
    if n<3:
        print(0)
        continue
    ans=0
    left=0
    right=1
    while right<n:
        while right<n-1 and a[right]<a[left]:
            right+=1
        up=min(a[left],a[right])
        for h in a[left+1:right]:
            ans+=up-h
        left=right
        right+=1
    print(ans)