if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        symbols = input()
        stack = []
        pre = '0'
        for j in range(len(symbols)):
            isover = 0
            if len(stack) == 0:
                if symbols[j] in {'[', '(', '{'}:
                    stack.append(symbols[j])
                    pre = symbols[j]
                else:
                    print('not balanced')
                    isover = 1
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
                            isover = 1
                            break
                        else:
                            pre = stack[len(stack) - 1]
                    elif symbols[j] == ')' and pre == '(':
                        stack.pop()
                        if len(stack) == 0:
                            print('balanced')
                            isover = 1
                            break
                        else:
                            pre = stack[len(stack) - 1]
                    elif symbols[j] == '}' and pre == '{':
                        stack.pop()
                        if len(stack) == 0:
                            print('balanced')
                            isover = 1
                            break
                        else:
                            pre = stack[len(stack) - 1]
            if isover==0:
                print('not balanced')
