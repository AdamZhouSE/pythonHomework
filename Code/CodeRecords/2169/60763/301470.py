def postfixEval(postfixExpr):
    operandStack = list()
    tokenList = postfixExpr.split()
    for token in tokenList:
        if token in "0123456789":
            operandStack.append(int(token))
        else:
            operand2 = operandStack.pop()  # 操作数2
            operand1 = operandStack.pop()  # 操作数1
            result = doMath(token, operand1, operand2)
            operandStack.append(result)
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

T = int(input())
for i in range(T):
    s = list(input())
    t = (' ').join(s)
    # print(t)
    print(postfixEval(t))