def func13():
    n = eval(input())
    arr = list(map(int, input().split()))
    ans = []
    for i in range(n - 1, -1, -1):
        if ans.count(arr[i]) == 0:
            ans.insert(0, arr[i])
    print(len(ans))
    for i in range(0, len(ans) - 1):
        print(ans[i], end=" ")
    print(ans[-1])


func13()