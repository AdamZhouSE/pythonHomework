def simplify(x: str) -> str:
    tmp = ''
    for i in range(len(x)):
        tmp += '/' + x[i] if x[i] == '-' or x[i] == '+' else x[i]
    tmp = tmp.split('/')
    # ax+b
    a, b = 0, 0
    for i in tmp:
        if i[-1] == 'x':
            if len(i[:-1]) == 0 or i[:-1] == '+':
                a += 1
            elif i[:-1] == '-':
                a += -1
            else:
                a += int(i[:-1])
        else:
            b += int(i)
    res = str(a) + 'x' + '+' + str(b) if b >= 0 else str(a) + 'x' + str(b)
    return res


def sign_reverse(x: str) -> str:
    x = list(x)
    if x[0] != '-':
        x = ['+'] + x
    for i in range(len(x)):
        if x[i] == '+':
            x[i] = '-'
        elif x[i] == '-':
            x[i] = '+'
    return ''.join(x)


left, right = map(str, input().split('='))
right = sign_reverse(right)
total = list(map(int, simplify(left + right).split('x')))
if total[0] == 0:
    if total[1] == 0:
        print('Infinite solutions')
    else:
        print('No solution')
else:
    print('x=' + str((-total[1]) / total[0]))
