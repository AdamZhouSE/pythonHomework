def d(n):
    for i in range(0, n):
        t = []
        [t.append(i) for i in [i for i in input()] if not i in t]
        print(''.join(t))


if __name__ == '__main__':
    d(int(input()))