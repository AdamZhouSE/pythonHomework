def func22():
    n = eval(input())
    arr = []
    for _ in range(0, n):
        arr.append(list(map(int, input().split())))
    res = [max(arr[0])]
    ans = True
    for i in range(1, n):
        tem1 = max(arr[i])
        tem2 = min(arr[i])
        if tem1 <= res[-1]:
            res.append(tem1)
        elif tem2 <= res[-1]:
            res.append(tem2)
        else:
            ans = False
            break
    if ans:
        print("YES")
    else:
        print("NO")


func22()
