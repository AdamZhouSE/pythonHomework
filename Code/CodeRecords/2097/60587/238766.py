numerator = int(input())
denominator = int(input())
if numerator == '0':
    print('0')
num, remainder = divmod(abs(numerator), abs(denominator))
if numerator * denominator < 0:
    sign = '-'
else:
    sign = ''
fraction = [sign + str(num)]
if remainder == 0:
    print(''.join(fraction))
else:
    fraction.append('.')
    dic = {}
    while remainder != 0:
        if remainder in dic:
            fraction.insert(dic[remainder], '(')
            fraction.append(')')
            break
        dic[remainder] = len(fraction)
        n, remainder = divmod(remainder * 10, abs(denominator))
        fraction.append(str(n))
    print(''.join(fraction))

