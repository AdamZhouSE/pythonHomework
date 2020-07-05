a = int(input())
for i in range(a):
    t = input()
    tL = input().split()
    l = []
    for var in tL:
        l.append(int(var))
    d = {}
    for var in l:
        if var not in d.keys():
            d[var] = 1
        else:
            d[var] += 1
    result = 0
    for key, value in d.items():
        result += value // 2
    print(result * 2)