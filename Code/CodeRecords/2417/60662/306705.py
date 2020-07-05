def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


num = list(map(int, input().split(',')))
if len(num) == 0:
    print('False')
else:
    d = num[0]
    for i in range(1, len(num)):
        d = gcd(d, num[i])
    if d == 1:
        print('True')
    else:
        print('False')