T = int(input())
while T > 0:
    T -= 1
    s = input()

    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = []
    postfixList = []
    tokenList = list(s)
    # tokenList.reverse()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            postfixList.append(token)
        elif token == '(':
            opStack.append(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not len(opStack) == 0) and (prec[opStack[0]] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.append(token)

    while not len(opStack) == 0:
        postfixList.append(opStack.pop())
    print(''.join(postfixList))