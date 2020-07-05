def s2():
    import itertools
    string = input().split()
    n = int(string[0])
    c = int(string[1])
    f = int(string[2])

    grade = []
    money = []
    index = []

    for i in range(c):
        s = input().split()
        grade.append(int(s[0]))
        money.append(int(s[1]))
        index.append(i)

    comb = list(itertools.combinations(index, n))
    max_middle = -1

    for l in comb:
        account = 0
        for i in l:
            account += money[i]
        if account > f:
            continue
        now = []
        for i in l:
            now.append(grade[i])
        now = sorted(now)

        if now[n//2] > max_middle:
            max_middle = now[n//2]

    print(max_middle, end="")


s2()