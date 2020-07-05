def func32():
    arr = list(map(int, input().split()))
    n = arr[0]
    m = arr[1]
    a = []
    b = []
    c = []
    for _ in range(0, n):
        arr = list(map(int, input().split()))
        a.append(arr[0])
        b.append(arr[1])
        c.append(arr[0] - arr[1])

    need = sum(a) - m
    ans = 0
    while need > 0 and sum(c)>0:
        val = max(c)
        c[c.index(val)] = 0
        need -= val
        ans += 1
    if need>0:
        print(-1)
    else:
        print(ans)


func32()
