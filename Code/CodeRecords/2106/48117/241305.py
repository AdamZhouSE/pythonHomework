s = input()
numStack = []
opStack = []

for op in s:
    if op == ' ':
        continue
    elif op >= '0' and op <= '9':
        numStack.append(op)
    elif op != ')':
        opStack.append(op)
    else:
        while opStack[-1] != '(':
            operator = opStack[-1]
            del opStack[-1]
            num2 = numStack[-1]
            del numStack[-1]
            num1 = numStack[-1]
            del numStack[-1]
            if operator == '+':
                numStack.append(str(int(num1) + int(num2)))
            else:
                numStack.append(str(int(num1) - int(num2)))
        del opStack[-1]

while not len(opStack) == 0:
    operator = opStack[0]
    del opStack[0]
    num1 = int(numStack[0])
    del numStack[0]
    num2 = int(numStack[0])
    del numStack[0]
    if operator == '+':
        numStack.insert(0, str(int(num1) + int(num2)))
    else:
        numStack.insert(0, str(int(num1) - int(num2)))

print(numStack[0])