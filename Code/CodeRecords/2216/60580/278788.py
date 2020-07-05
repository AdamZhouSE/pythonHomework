from fractions import Fraction

def operation(f1, f2 ,c):

    if c == '+':
        return f1 + f2
    else:
        return f1 - f2

s = input()
l = s.split('/')
loperand = []
loperand.append(l[0])
loperator = []
for i in range(1, len(l)-1):
    loperand.append(l[i][0])
    loperand.append(l[i][2])
    loperator.append(l[i][1])
loperand.append(l[len(l)-1])
l1 = []
for i in range(len(loperand)//2):
    l1.append(Fraction(int(loperand[2*i]), int(loperand[2*i+1])))
result = l1[0]
for i in range(len(loperator)):
    result = operation(result, l1[i+1], loperator[i])
if int(result) == result:
    print(str(result) + '/1')
else:
    print(result)