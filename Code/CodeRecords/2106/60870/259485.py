str_expression = input()
str_expression = str_expression.replace(' ', '')
operand = []
operator = []
for ch in str_expression:
    if ch.isdigit():
        operand.append(ch)
        if len(operand) > 1:
            if '9' >= str(operand[-2]) >= '0':
                if operator[-1] == '+':
                    operand_1 = int(operand.pop())
                    operand_2 = int(operand.pop())
                    operand.append(operand_1 + operand_2)
                else:
                    operand_1 = int(operand.pop())
                    operand_2 = int(operand.pop())
                    operand.append(operand_2 - operand_1)
    elif ch == '(':
        operand.append(ch)
    elif ch == '+' or ch == '-':
        operator.append(ch)
    elif ch == ')':
        while operand[-2] != '(':
            if operator[-1] == '+':
                operand_1 = int(operand.pop())
                operand_2 = int(operand.pop())
                operand.append(operand_1 + operand_2)
            else:
                operand_1 = int(operand.pop())
                operand_2 = int(operand.pop())
                operand.append(operand_2 - operand_1)
        valid = operand.pop()
        operand.pop()
        operand.append(valid)
        if len(operand) > 1:
            if '9' >= str(operand[-2]) >= '0':
                if operator[-1] == '+':
                    operand_1 = int(operand.pop())
                    operand_2 = int(operand.pop())
                    operand.append(operand_1 + operand_2)
                else:
                    operand_1 = int(operand.pop())
                    operand_2 = int(operand.pop())
                    operand.append(operand_2 - operand_1)
print(operand[0])