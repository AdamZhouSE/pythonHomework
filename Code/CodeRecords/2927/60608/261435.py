def func31():
    arr = list(map(int, input().split()))
    n, d = arr[0], arr[1]
    m = eval(input())
    for _ in range(0, m):
        arr = list(map(int, input().split()))
        x, y = arr[0], arr[1]
        sum1 = abs(x + y - d) + abs(x + y - 2 * n + d)
        sum2 = abs(x - y - d) + abs(x - y + d)
        if sum1 == 2 * (n - d) and sum2 == 2 * d:
            print("YES")
        else:
            print("NO")


func31()
