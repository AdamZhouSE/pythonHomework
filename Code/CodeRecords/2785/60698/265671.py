# 26
def test():
    n = int(input())
    angle = []
    sign = []
    for i in range(0, n):
        angle.append(int(input()))
    res = spin(angle, sign, n)
    if res:
        print("YES")
    else:
        print('NO')


def spin(angle, sign, n):
    if len(sign) == n:
        expr = ''
        for i in range(0, n):
            expr = expr + sign[i] + str(angle[i])
        sum = eval(expr)
        if sum % 360 == 0:
            return True
        else:
            return False
    else:
        for i in range(0, 2):
            if i == 0:
                sign.append('-')
            else:
                sign.append('+')
            if spin(angle, sign, n):
                return True
            else:
                sign.pop()
        return False


test()
