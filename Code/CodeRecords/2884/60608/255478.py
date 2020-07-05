def func5():
    res = list(map(int, input().split()))
    n = res[0]
    k = res[1]
    val = 0
    res = list(map(int, input().split()))
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if abs(res[i] - res[j]) <= k:
                val += 1
    print(2*val)


func5()