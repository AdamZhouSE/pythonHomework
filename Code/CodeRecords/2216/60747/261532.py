expression=input()
a=0
if expression[0] == '-':
    expression = '0/1' + expression
expression = expression.replace('-', '+-')
son_moms = []
expression=expression.split("+")
for fractions in expression:
    fractions=fractions.split("/")
    for j in range(len(fractions)):
        fractions[j]=int(fractions[j])
    son_moms.append(fractions)
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
    a=-1
if a!=-1:
    print(str(int(ans[0])) + "/" + str(int(ans[1])))