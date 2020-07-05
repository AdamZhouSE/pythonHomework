x=float(input())
n=int(input())
m = -n if n < 0 else n
p, q = 1, x
while m > 0:
    if (m&1) == 1:
        p *= q
    m //= 2
    q *= q
print('%.5f'%(1/p if n < 0 else p))