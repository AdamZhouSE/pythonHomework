def f(s):
    if len(s) == 1:
        return [s]
    else:
        start=s[0]
        t=f(s[1:])
        for i in range(length):
            if t[i][0]>start:
                t.append(t[i])
                t[i].insert(0,start)
        return t




s = [int(x) for x in input().split(',')]
print(max(len(x) for x in f(s)))