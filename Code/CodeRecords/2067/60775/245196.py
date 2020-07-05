
num = int(input())
result = ''
thous = num // 1000 % 10
hund = num // 100 % 10
ten = num // 10 % 10
one = num // 1 % 10
if thous != 0:
    result += 'M'*thous

if hund != 0:
    if hund == 9:
        result += 'CM'
    elif 9 > hund > 4:
        result += 'D'+ 'C'*(hund-5)
    elif hund == 4:
        result += 'CD'
    else:
        result += 'C'*hund

if ten != 0:
    if ten == 9:
        result += 'XC'
    elif 9 > ten > 4:
        result += 'L'+ 'X'*(ten-5)
    elif ten == 4:
        result += 'XL'
    else:
        result += 'X'*ten

if one != 0:
    if one == 9:
        result += 'IX'
    elif 9 > one > 4:
        result += 'V'+ 'I'*(one-5)
    elif one == 4:
        result += 'IV'
    else:
        result += 'I'*one

print(result)