def fractionAddition(expression):
    def GCD(a, b):
        if a % b == 0:
            return b
        else:
            return GCD(b, a % b)

    def LCM(a, b):
        return a * b / GCD(a, b)

    fractions = []
    tmp = ""
    for ch in expression:
        if ch in "-+":
            if tmp:
                fractions.append(tmp)
                tmp = ""
        tmp += ch
    if tmp:
        fractions.append(tmp)

    numerators = [int(f.split("/")[0]) for f in fractions]
    denominators = [int(f.split("/")[1]) for f in fractions]

    from functools import reduce
    DOWN = reduce(LCM, denominators)   # 所有分母的最小公倍数
    UP = sum(up * (DOWN / down) for up, down in zip(numerators, denominators))
    s = abs(GCD(UP, DOWN))
    ans = "{}/{}".format(int(UP / s), int(DOWN / s))
    return ans


string = input()
print(fractionAddition(string))
