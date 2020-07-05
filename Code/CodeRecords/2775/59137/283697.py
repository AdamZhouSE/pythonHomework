def s23():
    t = int(input())
    for i in range(t):
        n = int(input())
        if abs(n) % 3 == 0:
            print(int(n/3 - 1), int(n/3), int(n/3 + 1))
        else:
            print(-1)


s23()