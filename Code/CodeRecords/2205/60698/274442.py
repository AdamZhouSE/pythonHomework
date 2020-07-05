def test():
    t = int(input())
    for _ in range(0, t):
        n = int(input())
        res = shakeHand(n)
        print(res)


def shakeHand(n):
    if n<1:
        return 1
    elif n == 2:
        return 1
    elif n == 4:
        return 2
    else:
        if (n // 2) % 2 == 0:
            res = 0
            for i in range(n // 2, n):
                if i % 2 == 0:
                    res = res + 2 * shakeHand(n-i-2)*shakeHand(i)
            return res
        else:
            res = 0
            res = res + shakeHand(n // 2 - 1) * shakeHand(n // 2 - 1)
            for i in range(n // 2, n):
                if i % 2 == 0:
                    res = res + 2 * shakeHand(n-i-2)*shakeHand(i)
            return res


test()