def func14():
    n = eval(input())
    arr = list(map(int, input().split()))
    ans = [0, 0]
    for i in range(0, n):
        if arr[i] == 1:
            ans[0] += 1
        else:
            ans[1] += 1
    if ans[1] >= ans[0]:
        print(ans[0])
    else:
        print(ans[1] + (ans[0] - ans[1]) // 3)


func14()