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
            res.append(stack.pop())
    [print(i, end=' ') for i in res]
    print()
