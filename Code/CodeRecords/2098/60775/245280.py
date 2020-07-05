def char(num):
    '''
    :param num: 整数,范围1~26
    :return: 对应的大写字母
    '''
    return chr(ord('A')-1+num)


order = int(input())
result = ''
while order > 0:
    if order == 26:
        result = char(26) + result
        order = 0
    else:
        remainder = order % 26
        result = char(remainder) + result
        order = order // 26
print(result)