def func33():
    dividend = int(input())
    divisor = int(input())
    if dividend == 0:
        print("0")
    else:
        negative = (dividend ^ divisor) < 0
        t = abs(dividend)
        d = abs(divisor)
        res = 0
        i = 31
        while i >= 0:
            if (t>>i) >= d:
                res += 1<<i
                t -= d<<i
            i -= 1
        if negative:
            print(-res)
        else:
            print(res)
    return
func33()