def func18():
    n: int = eval(input())
    arr: list = list(map(int, input().split()))
    res = []
    ans = 0
    tem = 0
    for i in arr:
        if res.count(i) == 1:
            res.remove(i)
            tem-=1
        else:
            tem += 1
            res.append(i)
            ans = max(ans, tem)

    print(ans)


func18()
