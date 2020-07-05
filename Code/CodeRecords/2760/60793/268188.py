for test in range(0, int(input())):
    temp = list(map(int, input().split()))
    n, money = temp[0], temp[-1]
    print((n // 2 + n % 2) * money)