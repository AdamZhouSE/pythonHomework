m = int(input())
for v in range(0, m):
    #a, b = map(int, input().split())
    num = int(input())
    f = [0]*(num+1)
    f[1] = 1
    if num>2:
        f[2] = 2
    ans = 1
    for i in range(3, num+1):
        f[i] = f[i - 1] + f[i - 2]
    ans = f[num]
    print(ans)