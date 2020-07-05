str_rome = input()
res = 0
i = 0
length = len(str_rome)
while i < length:
    if str_rome[i] == 'I':
        if i == length - 1:
            res = res + 1
            i = i + 1
        else:
            if str_rome[i + 1] == 'V':
                res = res + 4
                i = i + 2
            elif str_rome[i + 1] == 'X':
                res = res + 9
                i = i + 2
            else:
                res = res + 1
                i = i + 1
    elif str_rome[i] == 'V':
        res = res + 5
        i = i + 1
    elif str_rome[i] == 'X':
        if i == length - 1:
            res = res + 10
            i = i + 1
        else:
            if str_rome[i + 1] == 'L':
                res = res + 40
                i = i + 2
            elif str_rome[i + 1] == 'C':
                res = res + 90
                i = i + 2
            else:
                res = res + 10
                i = i + 1
    elif str_rome[i] == 'L':
        res = res + 50
        i = i + 1
    elif str_rome[i] == 'C':
        if i == length - 1:
            res = res + 100
            i = i + 1
        else:
            if str_rome[i + 1] == 'D':
                res = res + 400
                i = i + 2
            elif str_rome[i + 1] == 'M':
                res = res + 900
                i = i + 2
            else:
                res = res + 100
                i = i + 1
    elif str_rome[i] == 'D':
        res = res + 500
        i = i + 1
    elif str_rome[i] == 'M':
        res = res + 1000
        i = i + 1
print(res)
