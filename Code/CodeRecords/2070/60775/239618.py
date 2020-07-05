x = float(input())
n = int(input())

if n == 0:
    print(x)
else:
    result = 1.00000
    n_is_neg = True if n<0 else False
    n = abs(n)
    for i in range(n):
        result *= x
    if n_is_neg:
        result = 1 / result
    print('%.5f'%result)