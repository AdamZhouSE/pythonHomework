xs = int(input())
res = []


def aux(res, ind, one, five, ten):
    if ind > 5:
        res.append((five + one * (ind - 5)) if ind < 9 else
                   one + ten)
    else:
        res.append(one * ind if ind < 4 else
                   one + five if ind == 4 else
                   five)


th = xs // 1000
aux(res, th, 'M', '', '')
xs %= 1000
hu = xs // 100
aux(res, hu, 'C', 'D', 'M')
xs %= 100
te = xs // 10
aux(res, te, 'X', 'L', 'C')
xs %= 10
aux(res, xs, 'I', 'V', 'X')
print(''.join(res))
