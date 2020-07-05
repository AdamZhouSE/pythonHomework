t = int(input())
for i in range(t):
    n = int(input())
    li = [int(x) for x in input().split()]
    suf = li.copy()
    for i in range(n-2,-1,-1):
        suf[i]=max(li[i],suf[i+1])
    ans = []
    for i in range(n):
        if suf[i]==li[i]:
            ans.append(suf[i])
    print(*ans)