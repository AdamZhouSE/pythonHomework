def validchar(ch):
    if ch>='0' and ch<='9':
        return True
    if ch=='e' or ch=='.':
        return True

def removespace(str):
    index = 0
    while index < len(str) and str[index] == ' ':
        index += 1
    return str[index::]

def isdigit(ch):
    return ch >= '0' and ch <= '9'

def validstr(str):
    str = removespace(str)
    if len(str) == 0:
        return False

    #check first bit
    if not (isdigit(str[0]) or str[0] == '-'):
        return False
    #第一位是负号，第二位是零，第三位只能是小数点
    if len(str)>=3 and str[0] == '-' and str[1] == '0':
        if str[2] != '.':
            return False

    #第一位是0，后面只能跟小数点
    if len(str)>=2 and str[0] == '0':
        if str[1] != '.':
            return False

    #整数部分一直前进
    index = 0
    if str[0] == '-':
        index += 1
    while index < len(str):
        if not isdigit(str[index]):
            break
        index += 1
    #判断一下跳过整数部分的结果
    if index == len(str):
        return True
    elif not (str[index] == 'e' or str[index]=='.'):
        return False

    #遇到小数点，前进过小数部分
    if str[index] == '.':
        index += 1
        has_digit = False
        while index < len(str):
            if not isdigit(str[index]):
                break
            index += 1
            has_digit = True
        if not has_digit:
            return False
        if index == len(str):
            return True
        elif not str[index]=='e':
            return False

    #进入指数部分
    index += 1
    has_digit = False
    while index < len(str):
        if not isdigit(str[index]):
            return False
        index += 1
        has_digit = True
    if not has_digit:
        return False
    return True

if __name__ == "__main__":
    str = input()
    print(validstr(str))