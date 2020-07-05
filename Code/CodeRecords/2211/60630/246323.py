n, m = [int(p) for p in input("").split(' ')]
q = [['-', 0]]

def check(p, st) :
    if len(st) <= 0 :
        return 1
    if p <= 0 :
        return 0
    if ord(q[p][0]) == ord(st[0]) :
        return check(q[p][1], st[1 : ])
    return 0

for i in range(0, n) :
    s = input("")
    q.append([s[0], int(s[2 : ])])

for i in range(0, m) :
    s = input("")
    res = 0
    for j in q :
        if ord(j[0]) == ord(s[0]) :
            res += check(j[1], s[1 : ])

    print(res)
