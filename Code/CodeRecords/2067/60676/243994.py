def transformer(num):
    copy = num
    res = ''
    while copy > 0:
        if copy // 1000 > 0:
            res += copy // 1000 * 'M'
            copy %= 1000
        elif copy >= 900:
            res += 'CM'
            copy %= 900
        elif copy >= 500:
            res += 'D'
            copy %= 500
        elif copy >= 400:
            res += 'CD'
            copy %= 400
        elif copy >= 100:
            res += copy // 100 * 'C'
            copy %= 100
        elif copy >= 90:
            res += 'XC'
            copy %= 90
        elif copy >= 50:
            res += 'L'
            copy %= 50
        elif copy >= 40:
            res += 'XL'
            copy %= 40
        elif copy >= 10:
            res += copy // 10 * 'X'
            copy %= 10
        elif copy >= 9:
            res += 'IX'
            copy %= 9
        elif copy >= 5:
            res += 'V'
            copy %= 5
        elif copy >= 4:
            res += 'IV'
            copy %= 4
        elif copy >= 1:
            res += copy * 'I'
            copy %= 1
    return res


print(transformer(int(input())))