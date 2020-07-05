def s9():
    t = int(input())
    for i in range(t):
        n = int(input())
        if n % 2 == 0:
            print(int(2 ** (3 ** ((n - 2) / 2))))
        else:
            print(int(2 ** (2 ** ((n - 1) / 2))))


s9()