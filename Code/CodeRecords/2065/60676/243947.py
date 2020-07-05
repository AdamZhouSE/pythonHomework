def transformer(string):
    new_str = string.replace(' ', '')
    index = 0
    res = ''
    if new_str[index] == '-':
        res += '-'
        index += 1
    while index < len(new_str) and new_str[index].isnumeric():
        res += new_str[index]
        index += 1
    if res == '' or res == '-':
        return 0
    res = int(res)
    if res > pow(2, 31) - 1:
        return pow(2, 31) - 1
    elif res < -pow(2, 31):
        return -pow(2, 31)
    else:
        return res


print(transformer(input()))
