# 18
inp = input()
inp = input()
a = inp.split()
for i in range(len(a)):
    a[i] = int(a[i])

def func(args):
    size = len(args)
    idx = 1
    i = args[0]
    while idx < size:
        j = args[idx]
        b = i if i < j else j
        a = i if i > j else j
        r = b
        while(r != 0):
            r = a % b
            if r != 0:
               a = b
               b = r
        f = i*j/b
        i = f
        idx += 1
    return f
lcm =int(func(a))

ok = True
for i in a:
    quotient=int(lcm/i)
    if (quotient-1)%2 !=0 and (quotient-1)%3 !=0:
        ok = False
if ok:
    print('Yes')
else:
    print('No')