import math
import sys


def excute(numerator, denominator):
    if numerator == 0: return "0"
    res = []
    if (numerator > 0) ^ (denominator > 0):
        res.append("-")
    numerator, denominator = abs(numerator), abs(denominator)

    a, b = divmod(numerator, denominator)
    res.append(str(a))

    if b == 0:
        return "".join(res)
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
    return "".join(res)


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

numerator = int(Input[0])
denominator = int(Input[1])
print(excute(numerator,denominator))
