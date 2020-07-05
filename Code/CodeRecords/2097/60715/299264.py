def fractionToDecimal(numerator, denominator):
    if numerator==denominator:
        return "1"
    if (numerator < 0 and denominator < 0):
        numerator, denominator = -numerator, -denominator
    u = (numerator < 0)^(denominator < 0)
    numerator = abs(numerator)
    denominator = abs(denominator)
    num = numerator % denominator
    if (num == 0):
        return str(numerator // denominator)
    s = str(abs(numerator) // denominator) + '.'
    q = {}
    l = []
    while (numerator < denominator):
        numerator = numerator * 10
        l.append(numerator)
        q[numerator] = numerator // denominator
    numerator = numerator % denominator * 10
    while (numerator not in q and numerator != 0):
        l.append(numerator)
        q[numerator] = numerator // denominator
        numerator = numerator % denominator
        numerator = numerator * 10
    for i in range(0, len(l)):
        if (numerator == l[i]):
            s = s + '('
        s = s + str(q[l[i]])
    if ('(' in s):
        s = s + ')'
    if (u):
        s = '-' + s
    return s
numerator=int(input())
denominator=int(input())
print(fractionToDecimal(numerator,denominator))
