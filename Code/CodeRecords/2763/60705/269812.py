if __name__ == '__main__':
    test = int(input())
    for t in range(0, test):
        [m, n] = list(map(int, input().split(" ")))
        if m < 2 ** (n-1):
            print(0)
        else:
            i = m - 2**(n-1)
            if i % 2 == 1:
                print(int((i**2-1) / 2 + 2))
            else:
                print(int(i**2 / 2 + 2))

