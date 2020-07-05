def priority(ch):
    if ch == '+' or ch == '-':
        return 1
    elif ch == '*' or ch == '/':
        return 2
    elif ch == '^':
        return 3
    elif ch == '(':
        return 4
    elif ch == ')':
        return 5
    else:
        return 0

def in2post(str):
    res = ""
    operand = []
    for ch in str:
        pri = priority(ch)
        #coperator
        if pri == 0:
            res = res + ch
        #'('
        elif pri == 4:
            operand.append(ch)
        #')'
        elif pri == 5:
            while True:
                op = operand.pop()
                if op == '(':
                    break
                else:
                    res = res + op

        else:
            while len(operand)>0 and priority(operand[-1]) >= pri:
                op = operand.pop()
                if op == '(':
                    operand.append('(')
                    break
                else:
                    res = res + op
            operand.append(ch)
    while len(operand) > 0:
        res += operand.pop()
    return res

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        str = input()
        ans.append(in2post(str))
    for res in ans:
        print(res)