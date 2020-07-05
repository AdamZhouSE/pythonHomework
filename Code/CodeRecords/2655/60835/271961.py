for h in range(int(input())):
    n = int(input())
    res = 1
    while True:
        if res >= n:
            break
        else:
            res = res * 2
    print(res)