for test in range(0, int(input())):
    input()
    ls = list(map(int, input().split()))
    result = abs(sum(ls[1:]) - sum(ls[0:1]))
    for i in range(1, len(ls)):
        s1 = ls[0:i]
        s2 = ls[i:]
        if abs(sum(s1) - sum(s2)) < result:
            result = abs(sum(s1) - sum(s2))
    print(result)
    