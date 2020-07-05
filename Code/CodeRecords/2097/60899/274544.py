def main():
    num = int(input())
    deno = int(input())
    str0 = fractionToDecimal(num,deno)
    print(str0)


def fractionToDecimal(numerator, denominator):
    """
    :type numerator: int
    :type denominator: int
    :rtype: str
    """
    if numerator==0:
        return "0"
    res = []
    if ((numerator>=0) is (denominator>=0)) == False:
        res.append("-")
    numerator, denominator = abs(numerator),abs(denominator)
    count = 0
    a = -1
    res.append(str(numerator//denominator))
    res.append(".")
    xiaoshu = []
    numerator = numerator%denominator*10
    while numerator and count<10:
        if a>=0:
            count += 1
            if str(numerator//denominator)!=xiaoshu[a+count]:
                count = 0
                a = -1
        if a==-1 and str(numerator//denominator) in xiaoshu:
            a = xiaoshu.index(str(numerator//denominator))
        xiaoshu.append(str(numerator//denominator))
        numerator = numerator%denominator*10
    if xiaoshu == []:
        res.pop()
    if numerator:
        xiaoshu = xiaoshu[:-11]
        while a>0 and xiaoshu[a-1] == xiaoshu[-1]:     #循环检测是否存在计数过程中的漏检
            a = a-1
            xiaoshu = xiaoshu[:-1]
        xiaoshu.insert(a, "(")
        xiaoshu.append(")")
    res = res + xiaoshu
    return "".join(res)
if __name__ == '__main__':
    main()