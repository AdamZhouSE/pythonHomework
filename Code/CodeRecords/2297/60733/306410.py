while True:
    try:
        a, b, c, start = int(input()), list(map(int, input().split())), int(input()), 0
        for i in range(c - 1):
            start += 2 ** i
        res = b[start:start + 2 ** (c - 1)]
        print(" ".join(map(str, res)) if res else "EMPTY")
    except:
        break