numerator = int(input())
denominator = int(input())
if numerator == 0:
    print("0")
else:
    res = []
    if (numerator > 0) ^ (denominator > 0):
        res.append("-")
    numerator, denominator = abs(numerator), abs(denominator)
    a, b = divmod(numerator, denominator)
    res.append(str(a))
    if b == 0:
        print("".join(res))
    else:
        res.append(".")
        loc = {b: len(res)}
        while b:
            b *= 10
            a, b = divmod(b, denominator)
            res.append(str(a))
            if b in loc:
                res.insert(loc[b], "(")
                res.append(")")
                break
            loc[b] = len(res)
        print("".join(res))