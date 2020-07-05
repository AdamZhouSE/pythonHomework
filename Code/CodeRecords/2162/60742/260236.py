x = float(input())
n = int(input())

if n==0:
    print(1.0*0)
else:
    neg = False
    res = 1
    if n<0:
        neg = True
        n = -n
    for i in range(n):
        res *= x
    if neg:
        res = 1/res
    print('{:.5f}'.format(res))