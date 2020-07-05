def func39():
    arr = list(map(int, input().split()))
    arr1=arr[:]
    n, m, d = arr[0], arr[1], arr[2]
    matrix = []
    res = set()
    for _ in range(0, n):
        t = list(map(int, input().split()))
        matrix.append(t)
        for i in t:
            res.add(i)
    ans = ((max(res) - min(res)) ) * n * m
    sub = set()
    for i in res:
        for j in res:
            if abs(i - j) % d != 0:
                sub.add(i)
                break
    res = res - sub

    if not res:
        print(-1)
    else:
        for k in res:
            tem = 0
            for i in range(0, n):
                for j in range(0, m):
                    tem += abs(matrix[i][j] - k) // d
            ans = min(ans, tem)
        print(ans)
        


func39()
