def f(x):
    if x == 2:
        return 2
    elif x == 5:
        return -1
    elif x == 3 or 6:
        return -1
    else:
        return x


if __name__ == '__main__':
    n = int(input())
    for i in range(0, n):
        num = int(input())
        print(f(num))
