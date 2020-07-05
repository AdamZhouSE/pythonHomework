"""
题目描述
    给定两个整数，被除数 dividend 和除数 divisor。
    将两数相除，要求不使用乘法、除法和 mod 运算符。
    返回被除数 dividend 除以除数 divisor 得到的商。
"""


def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    below = 1
    if dividend < 0 < divisor or divisor < 0 < dividend:
        below = -1

    dividend, divisor = abs(dividend), abs(divisor)
    if dividend < divisor:
        return 0
    elif divisor == 1:
        result = dividend * below
        if result >= 2 ** 31 - 1:
            return 2 ** 31 - 1
        return result

    result = len(range(divisor, dividend, divisor))
    if (result + 1) * divisor == dividend:
        result += 1
    return result * below


end = int(input())
sor = int(input())
print(divide(end, sor))
