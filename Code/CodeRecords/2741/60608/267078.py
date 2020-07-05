def func2():
    arr = eval(input())
    ans = 1
    tem = 1
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            tem += 1
        else:
            ans = max(ans, tem)
            tem = 1
    ans = max(ans, tem)
    print(ans)


func2()
