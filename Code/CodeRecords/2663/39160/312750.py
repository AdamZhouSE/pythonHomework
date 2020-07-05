def cal(n):
    if n == 2:
        return 7
    return cal(n-1) + 7 + 4*(n-2)

t = int(input())

for i in range(t):
    n = int(input())
    if n == 1:
        ans = 3
    else:
        ans = 3+cal(n)
    print(ans)