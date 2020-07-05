Times = int(input(""))
while Times > 0 :
    Times -= 1
    n, x, y = [int(p) for p in input("").strip().split(' ')]
    a = [int(p) for p in input("").strip().split(' ')]
    b = [int(p) for p in input("").strip().split(' ')]

    res = 0
    for i in range(0, n) :
        res += a[i]
        b[i] -= a[i]
    b.sort(reverse = True)
    for i in range(0, y) :
        if b[i] <= 0 :
            break
        res += b[i]

    print(res)
