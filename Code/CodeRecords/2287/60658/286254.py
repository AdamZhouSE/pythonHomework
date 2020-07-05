t = int(input())
for i in range(t):
    n = int(input())
    li = [int(x) for x in input().split()]
    suf = [-1 for i in range(n)]
    for i in range(n-2,-1,-1):
        if li[i]<li[i+1]:
            suf[i]=li[i+1]
        elif li[i]<=suf[i+1]:
            suf[i]=suf[i+1]
        else:
            suf[i]=-1
    print(*suf)