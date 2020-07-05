import re
s = re.sub('-','+-',input()).split('=')
s1 = s[0].split('+')
s2 = s[1].split('+')
coeff = 0
cons = 0
for i in s1:
    if 'x' in i:
        if i=='x':
            coeff += 1
        elif i=='-x':
            coeff -= 1
        else:
            coeff += int(i[:-1])
    else:
        cons += int(i)
for i in s2:
    if 'x' in i:
        if i=='x':
            coeff -= 1
        elif i=='-x':
            coeff += 1
        else:
            coeff -= int(i[:-1])
    else:
        cons -= int(i)
if coeff==0:
    if cons==0:
        print("Infinite solutions")
    else:
        print("No solution")
else:
    print('x=',end='')
    print(-1*cons/coeff)