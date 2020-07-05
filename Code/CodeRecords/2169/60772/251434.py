import sys
import re

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        # 判断是否为空
        return self.items == []

    def push(self, item):
        # 压入一个元素，无返回值
        self.items.append(item)

    def pop(self):
        # 弹出一个元素
        return self.items.pop()

    def peek(self):
        # 返回top元素，不改变原Stack
        return self.items[len(self.items) - 1]

    def size(self):
        # 返回Stack的大小
        return len(self.items)

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = list(postfixExpr)
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

Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0, int(test)):
    #info = Input[begin].split()
    #N = int(info[0])

    s = Input[begin]

    begin += 1

    str = ""
    for i in range(0,len(s)-1):
        str += s[i]

    print(postfixEval(str))
    # execute(s,len(s))
