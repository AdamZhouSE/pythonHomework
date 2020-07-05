questNum = int(input())

for quest in range(questNum):
    s = input()
    c = list(input())
    realC = []
    for w in c:
        realC.append(w)
    count = 0
    w = 0
    while w < len(s):
        if s[w] in c:
            if len(c) == len(realC):
                returnIndex = w
            del c[c.index(s[w])]
        else:
            if len(c) < len(realC):
                c.clear()
                for i in realC:
                    c.append(i)
                w = returnIndex

        if len(c) == 0:
            count += 1
            for i in realC:
                c.append(i)
            w = returnIndex

        w += 1
    print(count)