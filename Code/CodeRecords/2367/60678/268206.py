k = int(input())
if k % 2 == 0:
    print(-1)
else:
    num = 1
    len = 1
    while num < 10 ** 5:
        if num % k == 0:
            print(len)
            break
        else:
            len += 1
            num = int('1' * len)