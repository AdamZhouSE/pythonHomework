def f(n, d):
    if d == 0:
        return 1
    else:
        return f(n, d-1)**n + 1


if __name__ == '__main__':
    [n, d] = list(map(int, input().split(" ")))
    print(f(n, d) - f(n, d-1))
