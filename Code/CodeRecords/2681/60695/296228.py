t = int(input())
for i in range(t):
    n = int(input())
    cnt = 1
    while n > 1:
        if n % 2 == 1:
            n = n - 1
            cnt += 1
        else:
            n = n // 2
            cnt += 1
    print(cnt)
