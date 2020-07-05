"""
题目描述
    实现一个基本的计算器来计算一个简单的字符串表达式的值。
    字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格
"""


def calculate(s):
    """
    :type s: str
    :rtype: int
    """
    num = 0
    ans = 0
    sign = 1
    stack = []

    for c in s:
        if c.isnumeric():
            num = num * 10 + int(c)
        elif c == '+':
            ans += sign * num
            sign = 1
            num = 0
        elif c == '-':
            ans += sign * num
            sign = -1
            num = 0
        elif c == '(':
            stack.append(ans)
            stack.append(sign)
            sign = 1
            ans = 0
        elif c == ')':
            ans += sign * num
            ans *= stack.pop()
            ans += stack.pop()
            num = 0
    return ans + sign * num


print(calculate(input()))