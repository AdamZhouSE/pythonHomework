def isdigit(ch):
    if ch >= '0' and ch <= '9':
        return True
    return False

def postfixEval(str):
    operand = []
    for ch in str:
        if isdigit(ch):
            operand.append(int(""+ch))
        else:
            op2 = operand.pop()
            op1 = operand.pop()
            if ch == '+':
                operand.append(op1 + op2)
            elif ch == '-':
                operand.append(op1 - op2)
            elif ch == '*':
                operand.append(op1 * op2)
            elif ch == '/':
                operand.append(op1 / op2)
    return operand.pop()

if __name__ == "__main__":
    testNo = int(input())
    ans = []
    for i in range(testNo):
        str = input()
        ans.append(postfixEval(str))
    for res in ans:
        print(res)