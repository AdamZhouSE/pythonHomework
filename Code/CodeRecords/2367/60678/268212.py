k = int(input())
over = False
if k % 2 == 0:
    print(-1)
    over = True
else:
    num = 1
    len = 1
    while num < 10 ** 5:
        if num % k == 0:
            print(len)
            over = True
            break
        else:
            len += 1
            num = int('1' * len)
if not over:
    print(-1)