import re, math


def calculate(a, b):
    sign = [a[0], b[0]]
    a = ''.join(a[1:]).split('/')
    b = ''.join(b[1:]).split('/')
    res = [0, '/', 1]  # 初始化计算结果为0
    numerator = [int(sign[0] + a[0]), int(sign[1] + b[0])]
    denominator = [int(a[-1]), int(b[-1])]
    res[0] = str(numerator[0] * denominator[1] + numerator[1] * denominator[0])
    res[-1] = str(denominator[0] * denominator[1])
    return res


s = input()
sign = []
if s[0] != '-':
    s = '+' + s
for i in s:
    if i == '+' or i == '-':
        sign.append(i)
data = re.split('[+-]', s)[1:]
for i in range(len(data)):
    data[i] = sign[i] + data[i]
tmp = data[0]
for i in range(1, len(data)):
    tmp = calculate(tmp, data[i])
# 化简
if tmp[0] == '0':
    print('0/1')
else:
    gcd = math.gcd(abs(int(tmp[0])), int(tmp[-1]))
    tmp[0] = str(int(tmp[0]) // gcd)
    tmp[-1] = str(int(tmp[-1]) // gcd)
    print(''.join(tmp))
