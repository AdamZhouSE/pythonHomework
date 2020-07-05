dic = {
    'I':1  ,  'V':5  ,  'X':10  ,
    'L':50 ,  'C':100,  'D':500 ,  'M':1000
}

def first(ro):
    '''
    :param s:连续两个罗马符号
    :return: 第一个罗马符号实际值（int，有正负）
    '''
    first = dic[ro[0]]
    second = dic[ro[1]]
    if first<second:
        return -1 * first
    else:
        return first

Ro = input()
result = 0
for i in range(len(Ro)-1):
    result += first(Ro[i:i+2])
result += dic[Ro[-1]]
print(result)