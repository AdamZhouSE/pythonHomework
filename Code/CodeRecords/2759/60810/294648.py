'''
给定范围[m..n]。您的任务是找到在给定范围内被a或b整除的整数数量。
'''


def isIn(tmp, ans):
    for i in range(0, len(ans)):
        if tmp == ans[i]:
            return True
    return False


def findAns(m, n, a, b):
    ans = []
    for i in range(m, n + 1):
        if i % a == 0:
            if isIn(i, ans):
                continue
            else:
                ans.append(i)
    for j in range(m, n + 1):
        if j % b == 0:
            if isIn(j, ans):
                continue
            else:
                ans.append(j)
    print(len(ans))
    
    
t = int(input())
for i in range(0, t):
    inp = input().split(' ')
    m = int(inp[0])
    n = int(inp[1])
    a = int(inp[2])
    b = int(inp[3])
    findAns(m, n, a, b)