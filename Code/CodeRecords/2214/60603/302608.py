def xushu(x, y):
    lisx = x.split('+')
    lisy = y.split('+')
    a1 = int(lisx[0])
    a2 = int(lisx[1][:-1])
    a3 = int(lisy[0])
    a4 = int(lisy[1][:-1])
    ans0 = a1 * a3 - a2 * a4
    ans1 = a1 * a4 + a2 * a3
    result = str(ans0) + '+' + str(ans1) + 'i'
    print(result)
x = input()
y = input()
xushu(x, y)