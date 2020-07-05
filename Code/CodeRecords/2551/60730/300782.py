n, m = map(int, (input().strip().split(" ")))
temp = {}
ans = 0
for j in range(n):
    temp[j + 1] = 0
for i in range(m):
    c, a, b = map(int, (input().strip().split(" ")))
    if c == 0:
        for k in range(a - 1, b):
            if temp[k + 1] == 0:
                temp[k + 1] = 1
            else:
                temp[k + 1] = 0
    else:
        for k in range(a - 1, b):
            if temp[k + 1] == 1:
                ans += 1
        print(ans)
        ans = 0
