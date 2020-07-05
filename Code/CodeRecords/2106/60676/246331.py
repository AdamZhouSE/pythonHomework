# 实现一个基本的计算器来计算一个简单的字符串表达式的值。
# 字符串表达式可以包含左括号 ( ，右括号 ) ，加号 + ，减号 - ，非负整数和空格   。


def calculate(string):
    stack = []
    res = 0
    index = 0
    while index < len(string):
        if string[index].isnumeric():
            num = string[index]
            while index+1 < len(string) and string[index+1].isnumeric():
                num += string[index+1]
                index += 1
            stack.append(int(num))
        elif string[index] == '(' or string[index] == '+' or string[index] == '-':
            stack.append(string[index])
        elif string[index] == ')':
            temp = stack.pop(-1)
            while stack[-1] != '(':
                if stack.pop(-1) == '+':
                    temp += stack.pop(-1)
                else:
                    temp = stack.pop(-1) - temp
            stack.pop(-1)
            stack.append(temp)
        index += 1

    if len(stack) > 0:
        temp = stack.pop(0)
        while len(stack) > 0:
            if stack.pop(0) == '+':
                temp += stack.pop(0)
            else:
                temp -= stack.pop(0)
        res += temp
    return res


print(calculate(input()))