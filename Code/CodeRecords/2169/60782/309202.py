"""
题目描述

给定后缀表达式，任务是评估表达式并打印最终值。运算符将仅包括基本算术运算符，例如*，/，+和-。

输入描述

输入的第一行将包含一个整数T，表示测试用例的数量。然后是T测试用例。每个测试用例都包含一个后缀表达式。1 <= T <= 100；1 <= 表达式长度 <= 100

输出描述

对于每个测试用例，请在新行中评估后缀表达式并打印该值。
"""
# 后缀表达式求值
from pip._vendor.progress.counter import Stack


def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()
    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()  # 操作数2
            operand1 = operandStack.pop()  # 操作数1
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
    return operandStack.pop()


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


times = int(input())
while times > 0:
    times -= 1
    s = input()
    print(postfixEval(s))
