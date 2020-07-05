import math
import sys


def calculate(s):
    stack = []
    operand = 0
    res = 0 
    sign = 1  

    for ch in s:
        if ch.isdigit():
            operand = (operand * 10) + int(ch)

        elif ch == '+':
            res += sign * operand
            sign = 1
            operand = 0

        elif ch == '-':

            res += sign * operand
            sign = -1
            operand = 0

        elif ch == '(':
            stack.append(res)
            stack.append(sign)
            sign = 1
            res = 0

        elif ch == ')':
            res += sign * operand
            res *= stack.pop()  
            res += stack.pop()  
            operand = 0

    return res + sign * operand


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

s = Input[0]
print(calculate(s))
