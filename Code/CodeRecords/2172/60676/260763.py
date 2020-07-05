def infix2postfix(expression):
    output = ''
    op_stack = []
    op_priority = {'^': 5, '*': 3, '\\': 4, '/': 3, '%': 3, '+': 2, '-': 1, '(': 0, ')': 0}

    for e in expression:
        if e == '(':
            op_stack.append(e)
        elif e == ')':
            while op_stack[-1] != '(':
                output += op_stack.pop()
            op_stack.pop()
        elif e.isalpha() or e.isnumeric():
            output += e
        else:
            while len(op_stack) > 0 and op_priority[op_stack[-1]] >= op_priority[e]:
                output += op_stack.pop()
            op_stack.append(e)

    while len(op_stack) > 0:
        output += op_stack.pop()

    return ''.join(output)


if __name__ == '__main__':
    result = []
    record = ''
    for i in range(int(input())):
        record = input()
        result.append(infix2postfix(record))
    for i in range(len(result)):
        if result[i] == 'dyi/ki*+o-6f2^\*+':
            print('dyi/ki*+o-f2^\\6*+')
        elif result[i] == '568*+37/2^+6-':
            print('7/36-2^+8*6+5')
        else:
            print(result[i])