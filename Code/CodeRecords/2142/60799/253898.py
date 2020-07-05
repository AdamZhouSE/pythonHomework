T = int(input())
for ttt in range(T):
    strList = list(input().strip())
    left = 0
    res = []
    stack = []
    for i in strList:
        if i == '(':
            left += 1
            stack.append(left)
            res.append(left)
        if i == ')':
            left -= 1
            res.append(stack.pop())
    print(' '.join([str(i) for i in res]))