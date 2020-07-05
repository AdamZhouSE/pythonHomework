"""
题目描述
    给定两个二进制字符串，返回他们的和（用二进制表示）。
    输入为非空字符串且只包含数字 1 和 0。
"""


def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    '''
    说明：对于其中类型转化问题，可以自行百度相关的知识。
    '''
    a = int(a)
    b = int(b)
    result = list(str(a + b))
    for i in range(len(result) - 1, 0, -1):  # 从后往前遍历
        if (result[i] == '2'):  # 对数码位为2的情况进行处理
            result[i] = '0'
            result[i - 1] = str(int(result[i - 1]) + 1)
        elif (result[i] == '3'):  # 对数码位为3的情况进行处理
            result[i] = '1'
            result[i - 1] = str(int(result[i - 1]) + 1)
    if result[0] == '2':  # 对第一位数字单独进行考虑
        result[0] = '0'
        result.insert(0, '1')
    elif result[0] == '3':
        result[0] = '1'
        result.insert(0, '1')
    result = ''.join(result)
    return result


print(addBinary(input(), input()))