"""
题目描述
    给定一个正整数，返回它在 Excel 表中相对应的列名称。
"""
a = int(input())
answer = ""
while a // 26 != 0:
    a %= 26
    print(chr(a), end="")
print()