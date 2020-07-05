if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        symbols = input()
        stack = []
        pre = '0'
        for j in range(len(symbols)):
            if len(stack) == 0:
                if symbols[j] in {'[', '(', '{'}:
                    stack.append(symbols[j])
                    pre = symbols[j]
                else:
                    print('not balanced')
                    break
            else:
                if symbols[j] in {'[', '(', '{'}:
                    stack.append(symbols[j])
                    pre = symbols[j]
                else:
                    if symbols[j] == ']' and pre == '[':
                        stack.pop()
                        if len(stack) == 0:
                            print('balanced')
                            break
                        else:
                            pre = stack[len(stack) - 1]
                    elif symbols[j] == ')' and pre == '(':
                        stack.pop()
                        if len(stack) == 0:
                            print('balanced')
                            break
                        else:
                            pre = stack[len(stack) - 1]
                    elif symbols[j] == '}' and pre == '{':
                        stack.pop()
                        if len(stack) == 0:
                            print('balanced')
                            break
                        else:
                            pre = stack[len(stack) - 1]
            print('not balanced')
