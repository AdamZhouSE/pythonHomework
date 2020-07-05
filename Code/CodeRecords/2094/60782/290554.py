"""
题目描述
    验证给定的字符串是否可以解释为十进制数字。
"""
try:
    a = int(input())
    print(True)
except BaseException:
    print(False)
    print(a)
