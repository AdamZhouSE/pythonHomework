def func28():
    arr = list(map(int, input().split()))
    n = arr[0]
    r = arr[1]
    average = arr[2]
    a = []
    b = []
    for _ in range(0, n):
        arr = list(map(int, input().split()))
        a.append(arr[0])
        b.append(arr[1])
    need = n * average - sum(a)
    ans = 0
    while need > 0:
        index = b.index(min(b))
        num = min(need, r - a[index])
        need -= num
        ans += num * b[index]
        b[index] = max(b)
    print(ans)


func28()