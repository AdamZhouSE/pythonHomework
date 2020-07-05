T = int(input())
for _ in range(T):
    a = int(input())
    res = list()
    b = a
    while a > 0:
        res.append(a%2)
        a //= 2
    s = 0
    for i in range(len(res)):
        if res[i] == 0:
            s += pow(2, i)
    print(s, s+b)

