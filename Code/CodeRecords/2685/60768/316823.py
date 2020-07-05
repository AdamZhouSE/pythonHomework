def mini(n):
    res = ''
    for i in range(n):
        res = '0' + res
    while n > 9:
        res = '9' + res
        n -= 9
    res = str(n) + res
    return res


T = int(input())
for i in range(T):
    N = int(input())
    print(mini(N))