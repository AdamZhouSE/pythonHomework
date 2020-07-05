
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
    cd = gcd(c_1, cm)
    if cd < 0:
        cd = (-1) * cd
    c_1 //= cd
    cm //= cd
    return str(c_1) + '/' + str(cm)


inp = input()
fens = []
f_in = 0
for i in range(1, len(inp)):
    if inp[i] == '+' or inp[i] == '-':
        fens.append(inp[f_in:i])
        f_in = i
fens.append(inp[f_in:])
ans = fens[0]
for i in range(1, len(fens)):
    ans = plus(ans, fens[i])
print(ans)
