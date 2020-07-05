def cal(n,k):
    res = 1
    for i in range(n-1):
        res *=k
    return res

t = int(input())
for i in range(t):
    n,k = map(int,input().split(" "))
    print(cal(n,k))
