t = int(input())
for i in range(t):
    n = int(input())
    ans = []
    for i in range(1,n+1):
        a = i^(i//2)
        if (a+1)&a==0:
            ans.append(i)
    print(*ans)