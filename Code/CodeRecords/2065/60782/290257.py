"""
题目描述
    请你来实现一个 atoi 函数，使其能将字符串转换成整数。
    首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
    当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；
        假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
    当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；
        假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
    该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。
"""
"""
注意
    假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。
    在任何情况下，若函数不能进行有效的转换时，请返回 0。 
"""
"""
说明
    假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。
    如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。
"""


def myAtoi(str_in):
    res = []  # 有效的数字字符存储
    flag = True  # 默认值为True，一旦有整数字符出现，则标记为False

    numslist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(len(str_in)):
        if str_in[i] == ' ' and flag:  # 如果均为空格字符，且无非空字符出现继续
            continue

        if str_in[i] == '+' and flag:  # 如果“+”字符第一次出现，则添加到列表中，标记修改为False并继续
            res.append(str_in[i])
            flag = False
            continue

        if str_in[i] == '-' and flag:  # 如果“-”字符第一次出现，则添加到列表中，标记修改为False并继续
            res.append(str_in[i])
            flag = False
            continue

        if str_in[i] not in numslist:  # 除过上述情况，如果字符不为数字，则直接退出迭代
            break
        else:
            res.append(str_in[i])  # 反之有数字出现,添加到列表中，并修改标记为False
            flag = False

    res = ''.join(res)  # 拼接字符串 
    if res == '-' or res == '' or res == '+':
        return 0
    else:
        res = int(res)

    if res > 2 ** 31 - 1:  # 特殊情况处理
        return 2 ** 31 - 1
    if res < -2 ** 31:
        return -2 ** 31
    else:
        return res


print(myAtoi(input()))
