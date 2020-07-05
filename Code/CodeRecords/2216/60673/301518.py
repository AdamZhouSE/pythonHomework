import re

def lcm(a, b):
    return (a*b)/gcd(a,b)

def gcd(a, b):
    while(b != 0):
        temp = b
        b = a % b
        a = temp
    return a

expression = str(input())

string = re.findall(r'\d+/\d', expression)
operator = re.findall(r'\d([+-])\d',expression)
if expression[0] == '-':
    string[0] = '-' + string[0]
res = []
for item in string:
    res.append(item.split('/'))

help = int(res[0][1])
for i in range(1,len(res)):
    help = lcm(help, int(res[i][1]))
for i in range(len(res)):
    res[i][0] = int(res[i][0]) * help // int(res[i][1])

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