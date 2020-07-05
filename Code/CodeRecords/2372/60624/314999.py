def func20():
    t = int(input())
    while t > 0:
        t -= 1
        temp = list(map(int, input().split(" ")))
        n = temp[0]
        x = temp[1]
        y = temp[2]
        a = list(map(int, input().strip().split(" ")))
        b = list(map(int, input().strip().split(" ")))
        flag = [False for x in range(n)]
        c = []
        d = 0
        for i in range(n):
            c.append([a[i] - b[i], i])
            if a[i] - b[i] > 0:
                d += 1
        c.sort(key=lambda x: x[0], reverse=True)
        ans = 0
        if d >= x:
            for i in range(x):
                ans += a[c[i][1]]
                flag[c[i][1]] = True
            for i in range(n):
                if not flag[i]:
                    ans += b[i]
        else:
            if d + y >= n:
                for i in range(d):
                    ans += a[c[i][1]]
                    flag[c[i][1]] = True
                for i in range(n):
                    if not flag[i]:
                        ans += b[i]
            else:
                for i in range(n - y):
                    ans += a[c[i][1]]
                    flag[c[i][1]] = True
                for i in range(n):
                    if not flag[i]:
                        ans += b[i]
        print(ans)

    return
func20()