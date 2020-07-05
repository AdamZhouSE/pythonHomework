s = list(input())
num = []
temp = ''
for i in range(len(s)):
    if '0' <= s[i] <= '9':
        temp += s[i]
    elif s[i] == '-':
        if not temp == '':
            num.append(int(temp))
        temp = '-'
    elif s[i] == '+' or s[i] == '/':
        num.append(int(temp))
        temp = ''
num.append(int(temp))
top = []
bottom = []
for i in range(len(num)):
    if i % 2 == 0:
        top.append(num[i])
    else:
        bottom.append(num[i])


def lcm(x, y):
    if x > y:
        temp = x
    else:
        temp = y
    while True:
        if temp % x == 0 and temp % y == 0:
            break
        temp += 1
    return temp


b = bottom[0]
for i in range(1, len(bottom)):
    b = lcm(b, bottom[i])
a = 0
for i in range(len(top)):
    a += top[i] * (b // bottom[i])
if a == 0:
    print('0/1')
else:
    if a > b:
        temp = b
    else:
        temp = a
    while temp > 1:
        if a % temp == 0 and b % temp == 0:
            break
        temp -= 1
    a = str(a // temp)
    b = str(b // temp)
    if '-' in a and '-' in b:
        print(a[1:] + '/' + b[1:])
    elif '-' in b:
        print('-' + a + '/' + b[1:])
    else:
        print(a + '/' + b)