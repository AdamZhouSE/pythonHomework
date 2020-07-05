def myAtoi(str):
    s = str.strip()
    if not s:
        return 0

    sign = 1
    if s[0] == '-':
        sign = -1
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]

    num = ''
    for c in s:
        if c.isdigit():
            num += c
        else:
            break

    if not num:
        return 0

    num = int(num) * sign
    INT_MAX = 2 ** 31
    return min(max(num, -1 * INT_MAX), INT_MAX - 1)

s=input()
print(myAtoi(s))