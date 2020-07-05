'''
给定一个表示分数加减运算表达式的字符串，你需要返回一个字符串形式的计算结果。 这个结果应该是不可约分的分数，即最简分数。
如果最终结果是一个整数，例如 2，你需要将它转换成分数形式，其分母为 1。所以在上述例子中, 2 应该被转换为 2/1。
'''

import re

#求最小公倍数
def lcm(a, b):
    return (a*b)/gcd(a,b)

#求最大公因数
def gcd(a, b):
    while(b != 0):
        temp = b
        b = a % b
        a = temp
    return a

expression = str(input())

#划分表达式
string = re.findall(r'\d+/\d', expression)
operator = re.findall(r'\d([+-])\d',expression)
if expression[0] == '-':
    string[0] = '-' + string[0]
res = []
for item in string:
    res.append(item.split('/'))

#求所有分母的最小公倍数，使每个分数的分母都相同
help = int(res[0][1])
for i in range(1,len(res)):
    help = lcm(help, int(res[i][1]))
for i in range(len(res)):
    res[i][0] = int(res[i][0]) * help // int(res[i][1])

#求解加减运算
a = res[0][0]
res.pop(0)
while(operator):
    symbol = operator.pop(0)
    s = res.pop(0)
    if symbol == '+':
        a += s[0]
    else:
        a -= s[0]
if a == 0:
    print('0/1')
else:
    gys = gcd(abs(a), help)
    print('{0}/{1}'.format(int(a//gys), int(help//gys)))