num = int(input())
for _ in range(num):
    nxy = input().split(' ')
    n = int(nxy[0])
    x = int(nxy[1])
    y = int(nxy[2])
    a = input().split(' ')
    b = input().split(' ')
    try:
        a = [int(x) for x in a]
    except Exception as e:
        del a[len(a)-1]
        a = [int(x) for x in a]
    b = [int(x) for x in b]
    res = 0;
    compare = []
    for i in range(n):
        compare.append(a[i] - b[i])

    while x > 0:
        if max(compare) <= 0:
            break
        tempindex = compare.index(max(compare))
        res += a[tempindex]
        del compare[tempindex]
        del a[tempindex]
        del b[tempindex]
        x -= 1
    while y > 0:
        if len(compare)<=0 or min(compare) >= 0:
            break
        tempindex = compare.index(min(compare))
        res += b[tempindex]
        del compare[tempindex]
        del a[tempindex]
        del b[tempindex]
        y -= 1
    while len(a) != 0:
        res += a[len(a) - 1]
        del a[len(a) - 1]
    print(res)