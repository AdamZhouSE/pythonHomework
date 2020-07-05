expression = input()
if expression[0] == '-':
    expression = '0/1' + expression
expression = expression.replace('-', '+-')
son_moms = []
for fractions in expression.split('+'):
    son_moms.append(list(map(int, fractions.split('/'))))
ans = [0, 1]
for son_mom in son_moms:
    ans[0] = ans[0] * son_mom[1] + son_mom[0] * ans[1]
    ans[1] = ans[1] * son_mom[1]
    for div in range(2, abs(min(ans))):
        while (ans[0] % div == 0) and (ans[1] % div == 0):
            ans[0] /= div
            ans[1] /= div
if ans[0] == 0:
    print('0/1')
else:
    print(str(int(ans[0])) + "/" + str(int(ans[1])))