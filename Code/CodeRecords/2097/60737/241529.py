def frac_deci(numerator, denominator):
    if numerator == 0:
        return '0'
    res = []
    if numerator*denominator < 0:
        res.append('-')
    numerator, denominator = abs(numerator), abs(denominator)
    count = 0
    a = -1
    res.append(str(numerator // denominator))
    res.append('.')
    xiaoshu = []
    numerator = numerator % denominator * 10
    while numerator and count < 10:
        if a >= 0:
            count += 1
            if str(numerator // denominator) != xiaoshu[a + count]:
                count = 0
                a = -1
        if a == -1 and str(numerator // denominator) in xiaoshu:
            a = xiaoshu.index(str(numerator // denominator))
        xiaoshu.append(str(numerator // denominator))
        numerator = numerator % denominator * 10
    if xiaoshu == []:
        res.pop()
    if numerator:
        xiaoshu = xiaoshu[:-11]
        while a > 0 and xiaoshu[a - 1] == xiaoshu[-1]:
            a = a - 1
            xiaoshu = xiaoshu[:-1]
        xiaoshu.insert(a, '(')
        xiaoshu.append(')')
    res = res + xiaoshu
    return "".join(res)


if __name__ == "__main__":
    num = int(input())
    deno = int(input())
    print(frac_deci(num, deno))
