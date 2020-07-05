def func26():
    n = eval(input())
    arr = []
    for _ in range(0, n):
        arr.append(list(map(int, input().split())))
    ans = 0
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if arr[i][0] == arr[j][0] or arr[i][1] == arr[j][1]:
                ans += 1
    print(ans)


func26()
