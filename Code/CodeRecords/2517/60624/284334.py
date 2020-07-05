def func17():
    A = list(map(int, input().split(",")))
    B = list(map(int, input().split(",")))
    C = list(map(int, input().split(",")))
    D = list(map(int, input().split(",")))

    ans = 0
    ab_map = dict()

    for a in A:
        for b in B:
            ab_map[a+b] = ab_map.get(a+b,0) + 1

    for c in C:
        for d in D:
            s = -(c+d)
            if s in ab_map:
                ans += ab_map[s]
    print(ans)
    return 
func17()