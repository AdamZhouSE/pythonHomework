def s20():
    t = int(input())
    for i in range(t):
        n = int(input())
        if (n ** 0.5) % 1 == 0:
            print(1)
        else:
            print(0)


s20()