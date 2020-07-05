def do(pos):
    stack = []
    for x in pos:
        if ord('0') <= ord(x) <= ord('9'):
            stack.append(int(x))
        else:
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            if x == '+':
                result = num2 + num1
            elif x == '-':
                result = num2 - num1
            elif x == '*':
                result = num2 * num1
            elif x == '/':
                result = num2 / num1
            stack.append(result)
    return stack[0]

test = int(input())
for i in range(test):
    pos = input()
    print(do(pos))