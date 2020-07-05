def transformer(num):
    index = 0
    res = 0
    while index < len(num):
        if num[index:index+2] == 'IV':
            res += 4
            index += 2
        elif num[index:index+2] == 'IX':
            res += 9
            index += 2
        elif num[index:index+2] == 'XL':
            res += 40
            index += 2
        elif num[index:index+2] == 'XC':
            res += 90
            index += 2
        elif num[index:index+2] == 'CD':
            res += 400
            index += 2
        elif num[index:index+2] == 'CM':
            res += 900
            index += 2
        elif num[index:index+1] == 'I':
            res += 1
            index += 1
        elif num[index:index+1] == 'V':
            res += 5
            index += 1
        elif num[index:index+1] == 'X':
            res += 10
            index += 1
        elif num[index:index+1] == 'L':
            res += 50
            index += 1
        elif num[index:index+1] == 'C':
            res += 100
            index += 1
        elif num[index:index+1] == 'D':
            res += 500
            index += 1
        elif num[index:index+1] == 'M':
            res += 1000
            index += 1
    return res


print(transformer(input()))