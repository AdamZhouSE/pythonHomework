def func24():
    n = eval(input())
    arr = list(map(int, input().split()))
    ans = 0
    tem = 1
    for i in range(1, n):
        if arr[i] <= arr[i - 1] * 2:
            tem += 1
        else:
            ans = max(ans, tem)
            tem = 1
    ans = max(tem, ans)
    print(ans)


func24()
