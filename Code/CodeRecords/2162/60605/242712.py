
x = eval(input())
n = int(input())

a = abs(n)
res = 1.0
for i in range(0, int(a)):
    res *= x

if n < 0:
    print('%.5f' % (1.0/res))
else:
    print('%.5f' % res)