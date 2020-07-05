def tran(s):
    begin = False
    num = 0
    sign = 1
    i = 0
    while i < len(s):
        if not begin and s[i] != ' ':
            if s[i] == '-':
                begin = True
                sign = -1
                if i < len(s)-1:
                    i += 1
            elif s[i]>='0' and s[i]<='9':
                begin = True
            else:
                return 0
        if begin:
            if s[i]<'0' or s[i]>'9':
                break
            num *= 10
            num += int(s[i])-0
        i += 1
    num *= sign
    if num < int(-1*pow(2,31)):
        return int(-1*pow(2,31))
    elif num > int(pow(2,31)-1):
        return int(pow(2,31)-1)
    else:
        return num

s = input()

print(tran(s))
