for h in range(int(input())):
    n = int(input())
    cnt = 0
    while n > 0:
        if n % 2 != 0:
            cnt = cnt + 1
        n = n // 2
    if cnt % 2 == 0:
        print("even")
    else:
        print("odd")