def fractionToDecimal( numerator, denominator):
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


numerator = int(input())
denominator = int(input())
print(fractionToDecimal(numerator,denominator))