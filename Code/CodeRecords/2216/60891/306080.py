# 最大公约数
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while b != 0:
        a, b = b, a % b
    return a


# 最小公倍数
def lcm(a, b):
    return a * b // gcd(a, b)


def plus(a, b):
    a_12 = [int(i) for i in a.split('/')]
    b_12 = [int(i) for i in b.split('/')]
    a_1 = a_12[0]
    a_2 = a_12[1]
    b_1 = b_12[0]
    b_2 = b_12[1]
    cm = lcm(a_2, b_2)
    c_1 = (cm // a_2 * a_1) + (cm // b_2 * b_1)
    if c_1 == 0:
        return '0/1'
    cd = lcm(c_1, cm)
    c_1 //= cd
    cm //= cd
    return str(c_1) + '/' + str(cm)
