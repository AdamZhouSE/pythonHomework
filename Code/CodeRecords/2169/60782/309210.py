"""
题目描述

给定后缀表达式，任务是评估表达式并打印最终值。运算符将仅包括基本算术运算符，例如*，/，+和-。

输入描述

输入的第一行将包含一个整数T，表示测试用例的数量。然后是T测试用例。每个测试用例都包含一个后缀表达式。1 <= T <= 100；1 <= 表达式长度 <= 100

输出描述

对于每个测试用例，请在新行中评估后缀表达式并打印该值。
"""


# 后缀表达式求值


class Stack:
 
    def __init__(self):
 
        self.items = []
 
    def isEmpty(self):
 
        return self.items == []
 
    def push(self, item):
 
        self.items.append(item)
 
    def pop(self):
 
        return self.items.pop()
 
    def peek(self):
 
        return self.items[len(self.items)-1]
 
    def size(self):
 
        return len(self.items)
 
 
def postfix_calculate(s):
    """注意-号和/号的顺序问题"""
    stack = Stack()
    for x in s:
        if x.isdigit():
            stack.push(x)
        elif x == "+":
            a = stack.pop()
            b = stack.pop()
            stack.push(int(a)+int(b))
        elif x == "-":
            a = stack.pop()
            b = stack.pop()
            stack.push(int(b)-int(a))
        elif x == "*":
            a = stack.pop()
            b = stack.pop()
            stack.push(int(a)*int(b))
        elif x == "/":
            a = stack.pop()
            b = stack.pop()
            stack.push(int(b)/int(a))
 
    return stack.peek()




times = int(input())
while times > 0:
    times -= 1
    s = input()
    print(postfix_calculate(s))
