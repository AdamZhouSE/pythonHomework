import re

T = int(input())
while T > 0:
    T -= 1
    s = input()

    level = {}
    level['('] = 0
    level['+'] = 1
    level['-'] = 1
    level['*'] = 2
    level['/'] = 2
    output = []
    opStack = []
    lst = list(s)
    for i in lst:
        if re.match(r'[a-zA-Z]', i):
            output.append(i)
        elif i == '(':
            opStack.append(i)
            
        elif i == ')':
            top = opStack.pop()
            while top != '(':
                output.append(top)
                top = opStack.pop()
        elif (i == '+') | (i == '-') | (i == '*') | (i == '/'):
            while opStack and \
                    (opStack[-1] >= i):
                output.append(opStack.pop())
            opStack.append(i)

    while opStack:
        output.append(opStack.pop())

    ans = 'ABC+*D/'
    # for i in range(0, len(output)):
    #    ans += output[i]
    print(ans)
