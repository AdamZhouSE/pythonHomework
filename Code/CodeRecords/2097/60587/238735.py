numerator = int(input())
denominator = int(input())

num, remainder = divmod(abs(numerator), abs(denominator))
if numerator * denominator < 0:
    sign = '-'
else:
    sign = ''
fraction = [sign + str(num)]
if remainder == 0:
    print(''.join(fraction))

