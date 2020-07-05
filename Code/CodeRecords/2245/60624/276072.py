def func13():
    n = int(input())
    res = 0
    pre = None
    cur = 0
    while n:
        if n & 1:
            if pre is not None:
                res = max(res, cur - pre)
            pre = cur
        cur += 1
        n >>= 1
    print(res)
    return
func13()