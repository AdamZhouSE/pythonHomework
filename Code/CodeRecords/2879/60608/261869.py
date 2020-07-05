def func37():
    n = eval(input())
    arr = []
    arr1 = []
    arr2 = []
    ans = []
    for _ in range(0, n*n):
        arr.append(list(map(int, input().split())))
    for i in range(0, n * n):
        if arr1.count(arr[i][0]) == 0 and arr2.count(arr[i][1]) == 0:
            ans.append(i)
            arr1.append(arr[i][0])
            arr2.append(arr[i][1])
    for i in range(0, n - 1):
        print(ans[i] + 1, end=" ")
    print(ans[-1] + 1)


func37()
