if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        symbols = input()
        stack = []
        pre = '0'
        for j in range(len(symbols)):
            if symbols[j] in {'[', '(', '{'}:
                stack.append(symbols[j])
                pre = symbols[j]
            else:
                if (symbols[j] == ']' and pre == '[') or (symbols[j] == ')' and pre == '(') or (symbols[j] == '}' and pre == '{'):
                    stack.pop()
                    if len(stack) == 0:
                        pre = '0'
                    else:
                        pre = stack[len(stack) - 1]
                else:
                    stack.append(symbols[j])
                    break
        if len(stack) == 0:
            print('balanced')
        else:
            print('not balanced')
