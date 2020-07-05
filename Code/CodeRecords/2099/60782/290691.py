"""
题目描述
    给定一个Excel表格中的列名称，返回其相应的列序号。
"""


def titleToNumber(s):
    """
    :type s: str
    :rtype: int
    """
    result = 0
    for letter in s:
        result = result * 26 + ord(letter) - ord('A') + 1
    return result


print(titleToNumber(input()))
