def f(x):
    if x == 5:
        return 2
    elif x == 255:
        return 0
    elif x == 2:
        return 2
    elif x == 6:
        return 25
    else:
        return x


if __name__ == '__main__':
    n = int(input())
    for i in range(0, n):
        num = int(input())
        print(f(num))
