for h in range(int(input())):
    n = input().split()
    tem = input().split()
    x = []
    for a in tem:
        x.append(int(a))
    tem = input().split()
    y = []
    for a in tem:
        y.append(int(a))
    x.extend(y)
    x.sort()
    print(x[int(n[2]) - 1])