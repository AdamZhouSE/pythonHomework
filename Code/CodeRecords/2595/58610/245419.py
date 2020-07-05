for _ in range(eval(input())):
    a = list(map(int, input().split(' ')))
    print(a[1] ** (a[0] - 1))
