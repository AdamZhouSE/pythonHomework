t = eval(input())
for _ in range(t):
    n, x = [int(x) for x in input().split()]
    es = [int(x) for x in input().split()]
    want = set([x / e for e in es])
    # print(want)
    for e in es:
        if e in want and e ** 2 != x:
            print('Yes')
            break
    else:
        print('No')
