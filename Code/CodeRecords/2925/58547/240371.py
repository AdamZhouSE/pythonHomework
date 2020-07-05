def func():
    n = int(input())
    a = [(int(x) - 1) for x in input().split(" ")]
    b = [(int(x) - 1) for x in input().split(" ")]

    pos = [0] * n
    i = 0
    while i < n:
        pos[b[i]] = i
        i += 1

    c = [0] * n
    i = 0
    while i < n:
        c[i] = pos[a[i]]
        i += 1

    mx = -1
    ans = 0
    i = 0
    while i < n:
        if c[i] > mx:
            mx = c[i]
        else:
            ans += 1
        i += 1

    print(ans)


func()
