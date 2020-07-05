n, m = map(int, (input().strip().split(" ")))
temp = {}
ans = 0
for j in range(n):
    temp[j + 1] = 0
for i in range(m):
    c, a, b = map(int, (input().strip().split(" ")))
    if c == 1:
        for k in range(a - 1, b):
            temp[k + 1] = temp[k + 1] + 1
    else:
        for k in range(a - 1, b):
            test = temp[k + 1]
            if test > ans:
                ans = test
        print(ans)
