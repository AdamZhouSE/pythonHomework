t = int(input())
for i in range(t):
    n = int(input())
    li = [int(x) for x in input().split()]
    ans = []
    for i in range(n-1):
        if li[i]>li[i+1]:
            ans.append(li[i+1])
        else:
            ans.append(-1)
    ans.append(-1)
    print(*ans,end=" \n")