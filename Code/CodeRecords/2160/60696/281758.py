def solve(dividend, divisor):
    res = 0
    if divisor == 0:
        raise ArithmeticError
    if (divisor > 0 and dividend > 0) or (dividend < 0 and divisor < 0):
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            dividend -= divisor
            res += 1
        return res
    else:
        dividend = abs(dividend)
        divisor = -abs(divisor)
        while dividend >= -divisor:
            dividend += divisor
            res -= 1
        return res


if __name__ == '__main__':
    dividend = int(input())
    divisor = int(input())
    print(solve(dividend, divisor))
