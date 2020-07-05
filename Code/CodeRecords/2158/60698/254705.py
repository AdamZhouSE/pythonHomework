def atoi(s):
    s = str(s)
    s = s.strip()
    if len(s) == 0:
        print(0)
        return
    exist = False
    begin = 0
    digit_str = ''
    c_str = str(s[0])
    if c_str.isdigit() or ((c_str == '+' or c_str == '-') and len(s) != 1):
        exist = True
        digit_str = c_str
        begin = 0
        if not ((c_str == '+' or c_str == '-') and str(s[1]).isdigit()):
            exist = False
        if c_str.isdigit():
            exist=True
    if exist:
        for j in range(begin + 1, len(s)):
            c_str = str(s[j])
            if c_str.isdigit():
                digit_str = digit_str + c_str
            else:
                break
    else:
        print(0)
        return
    result = int(digit_str)
    if (result > 0):
        result = min(2 ** 31 - 1, result)
    else:
        result = max(-2 ** 31, result)
    print(result)


if __name__ == '__main__':
    atoi(input())
