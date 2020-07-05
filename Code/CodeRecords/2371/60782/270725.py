"""
题目描述
    贾维斯在计算字母数字字符回文率方面很弱。
    当钢铁侠忙于与灭霸战斗时，他需要启动音速冲动，但是贾维斯不会计算回文。
    给定一个包含字母数字字符的字符串S，找出字符串是否是回文，拯救钢铁侠。
"""
"""
输入描述
    输入的第一行包含T，即测试用例的数量。随后是T个测试用例。测试用例的每一行都包含字符串“S”。
"""
"""
输出描述
    如果字符串是回文，则输出的每一行都包含“ YES”，如果字符串不是回文，则输出“ NO”。
"""
times = int(input())
while times > 0:
    times = times - 1
    string = input()
    string = ''.join([x for x in string if x.isalpha()])
    string = string.lower()
    # print(string)
    l = list(string)
    l.reverse()
    re = "".join(l)
    if re == string:
        print("YES")
    else:
        print("NO")