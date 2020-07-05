def func14():
    t = int(input())
    while t > 0:
        t -= 1
        res = n = int(input())
        i = 0
        while n > 0:
            a = n % 2
            n = n // 2
            b = n % 2
            n = n // 2
            if a != b:
                if b == 1:
                    res -= pow(2,i)
                else:
                    res += pow(2,i)
            i += 2
        print(res)
    return
func14()