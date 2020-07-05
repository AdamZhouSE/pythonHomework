def func3():
    arr = eval(input())
    k = len(arr) // 3
    ans = []
    for i in arr:
        if ans.count(i) == 0 and arr.count(i) > k:
            ans.append(i)
    print(ans)


func3()
