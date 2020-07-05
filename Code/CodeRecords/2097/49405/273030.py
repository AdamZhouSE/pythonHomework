for t in range(1):
    n = int(input())
    d = int(input())
    if n >= d:
        if n % d == 0:
            print(n // d)
            continue
        print(n // d, end=".")
        n %= d
    else:
        print(0, end=".")
    s = []
    y = []
    ans = False
    while n != 0:
        n *= 10
        ns = n //d
        ny = n % d
        n %= d
        try:
            p = y.index(ny)
        except:
            p = -1
        if p < 0:
            s.append(ns)
            y.append(ny)
        else:
            for i in range(p):
                print(s[i], end="")
            print("(", end="")
            for i in range(p, len(s)):
                print(s[i], end="")
            print(")")
            ans = True
            break
    if not ans: print("".join(map(str, s)))