def f(x):
    if x == 2:
        return 2
    else:
        print(x)


if __name__ == '__main__':
    n = int(input())
    for i in range(0, n):
        num = int(input())
        print(f(num))
