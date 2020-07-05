

def solve():
    num = int(input())
    res = ''
    while num >= 1000:
        res += 'M'
        num = num - 1000
    if num >= 900:
        res += 'C'
        res += 'M'
        num = num - 900
    while num >= 500:
        res += 'D'
        num = num - 500
    if num >= 400:
        res += 'C'
        res += 'D'
        num = num - 400
    while num >= 100:
        res += 'C'
        num  = num - 100
    if num > 90:
        res += 'X'
        res += 'C'
        num = num - 90
    if num >= 50:
        res += 'L'
        num = num - 50
    if num >= 40:
        res += 'X'
        res += 'L'
        num = num - 40
    while num >= 10:
        res += 'X'
        num = num - 10
    if num >= 9:
        res += 'I'
        res += 'X'
        num = num - 9
    if num >= 5:
        res += 'V'
        num = num - 5
    if num >= 4:
        res += 'I'
        res += 'V'
        num = num - 4
    while num >= 1:
        res += 'I'
        num = num - 1

    print(str(res))

solve()