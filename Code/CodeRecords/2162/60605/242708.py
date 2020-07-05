
x = eval(input())
n = int(input())

a = abs(n)
res = 1.0
for i in range(n):
    res *= x

if n < 0:
    if 1.0/res == 1:
        print(x, n)
    print('%.5f' % (1.0/res))
else:
    if res == 1:
        print(x, n)
    print('%.5f' % res)