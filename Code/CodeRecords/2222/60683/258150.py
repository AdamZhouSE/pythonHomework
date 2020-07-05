ss = input().split('=')
xNum = [0] * 2
sumN = [0] * 2
for n in range(2):
    if '0' <= ss[n][0] <= '9':
        ss[n] = '+' + ss[n]
    p = 0
    for i in range(len(ss[n])):
        if ss[n][i] in ('-', '+'):
            if ss[n][i - 1] != 'x':
                temp = ''
                while p != i:
                    temp += ss[n][p]
                    p += 1
                if len(temp) > 0:
                    if len(temp) == 1:
                        temp += '1'
                    if temp[0] == '+':
                        sumN[n] += int(temp[1:])
                    elif temp[0] == '-':
                        sumN[n] -= int(temp[1:])
            # p = i
        if ss[n][i] == 'x':
            if p == 0 and ss[n][0] != '+':
                xNum[n] += 1
            else:
                temp = ''
                while p != i:
                    temp += ss[n][p]
                    p += 1
                if len(temp) == 1:
                    temp += '1'
                if temp[0] == '+':
                    xNum[n] += int(temp[1:])
                elif temp[0] == '-':
                    xNum[n] -= int(temp[1:])
            p = i + 1
    if p < len(ss[n]):
        temp = ''
        while p != len(ss[n]):
            temp += ss[n][p]
            p += 1
        if len(temp) == 1:
            temp += '1'
        if temp[0] == '+':
            sumN[n] += int(temp[1:])
        elif temp[0] == '-':
            sumN[n] -= int(temp[1:])
# print(xNum)
# print(sumN)

if xNum[0] == xNum[1]:
    if sumN[0] == sumN[1]:
        print('Infinite solutions')
    else:
        print('No solution')
else:
    print('x=', end='')
    print((sumN[1] - sumN[0]) / (xNum[0] - xNum[1]))
