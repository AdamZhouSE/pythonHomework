T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    res = ''
    while n > 0:
        tmp = n // 2
        remain = n % 2
        if tmp == 1:
            res += '4'
        else:
            res += '7'
        n = n // 2
    print(res)