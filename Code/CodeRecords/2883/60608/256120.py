def func16():
    arr: list = list(map(int, input().split()))
    n = arr[0]
    m = arr[1]
    flag = 0
    arr = []
    ans = [0, 0]
    for _ in range(0, n):
        arr.append(list(input()))
    for i in range(0, n):
        if arr[i].count("B") != 0 and flag == 0:
            flag = 1
            ans[0] = i
            tem1 = 0
            tem2 = m - 1
            while tem1 < m and arr[i][tem1] == 'W':
                tem1 += 1
            while tem2 >= 0 and arr[i][tem2] == "W":
                tem2 -= 1
            ans[1] = (tem1 + tem2) // 2 + 1

        if arr[i].count("B") == 0 and flag == 1:
            ans[0] = (i + ans[0]) // 2 + 1
            break

    if arr[-1].count("B") > 0:
        ans[0] = (ans[0] + n - 1) // 2 + 1

    print("%d %d" % (ans[0], ans[1]))


func16()
