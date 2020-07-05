T = int(input())
for ttt in range(T):
    nList = list(input().strip().lstrip(')').rstrip('('))
    stack = []
    resList = [False] * len(nList)
    for i in range(len(nList)):
        if nList[i] == '(':
            stack.append(i)
        else:
            if stack:
                resList[i] = resList[stack.pop()] = True
    res = tmp = 0
    for i in resList:
        if i:
            tmp += 1
            res = max(res, tmp)
        else:
            tmp = 0
    print(res)