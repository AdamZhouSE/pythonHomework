def isdigit(ch):
    return ch>='0' and ch<='9'

def evalExp(str):
    str = str.replace(" ","")
    #print(str)
    operator = []
    operand = []
    index = 0
    while index < len(str):
        if isdigit(str[index]):
            temp = 0
            while index<len(str) and isdigit(str[index]):
                temp *= 10
                temp += int(str[index])
                index += 1
            operand.append(temp)
        elif str[index]=='(':
            operator.append('(')
            index += 1
        elif str[index]==')':
            temp = operator.pop()
            if temp == '(':
                pass
            else:
                op2 = operand.pop()
                op1 = operand.pop()
                if temp == '+':
                    operand.append(op1 + op2)
                else:
                    operand.append(op1 - op2)
                operator.pop()
            index += 1
        else:
            if operator != [] and operator[-1] != '(':
                op2 = operand.pop()
                op1 = operand.pop()
                if operator.pop() == '+':
                    operand.append(op1+op2)
                else:
                    operand.append(op1-op2)
            operator.append(str[index])
            index += 1
    while operator != []:
        op2 = operand.pop()
        op1 = operand.pop()
        op = operator.pop()
        if  op == '+':
            operand.append(op1 + op2)
        else:
            operand.append(op1 - op2)

    print(operand[0])

if __name__ == "__main__":
    str = input()
    evalExp(str)