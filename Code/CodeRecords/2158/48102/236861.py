def str_to_int():
    string = input()
    str_len = len(string)
    res = []
    sign = 1
    for i in range(str_len):
        if string[i].isspace():
            continue
        elif string[i] != '+' and string[i] != '-' and not string[i].isdigit():
            break
        elif string[i] == '-' and (i + 1 < str_len and string[i+1].isdigit()):
            sign = -1
        elif string[i].isdigit():
            res.append(string[i])
            if i + 1 < str_len and (not string[i+1].isdigit()):
                break
    if len(res) == 0:
        return 0
    else:
        number = int(''.join(res)) * sign
        if number <= -2**31:
            return -2**31
        elif number >= 2**31 - 1:
            return 2**31 - 1
        else:
            return number


print(str_to_int())