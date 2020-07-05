"""
题目描述
    给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。
    如果小数部分为循环小数，则将循环的部分括在括号内。
"""


def fractionToDecimal(numerator, denominator):
    """
    :type numerator: int
    :type denominator: int
    :rtype: str
    """
    if numerator == 0:
        return '0'
    elif denominator == 0:
        return ''
    else:
        isNegative = (numerator < 0) ^ (denominator < 0)
        numerator = abs(numerator)
        denominator = abs(denominator)
        res = ''
        res += '-' if isNegative else ''
        res += str(numerator // denominator)
        numerator %= denominator
        if numerator == 0:
            return res
        else:
            res += '.'
            dic = {}
            while numerator:
                if numerator in dic:
                    start = dic[numerator]
                    end = len(res)
                    res = res[:start] + '(' + res[start:end] + ')'
                    return res
                dic[numerator] = len(res)
                res += str(numerator * 10 // denominator)
                numerator = numerator * 10 % denominator
            return res


print(fractionToDecimal(int(input(), int(input()))))
