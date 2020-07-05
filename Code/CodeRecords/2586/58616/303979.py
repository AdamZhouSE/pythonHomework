# LeetCode 1033
# 根据题给描述耐心分类即可
def numMovesStones(a, b, c):
    a, b, c = sorted([a, b, c])
    if b-a == 1 and c-b == 1:
        return [0, 0]
    elif b-a == 1 and c-b != 1:
        return [1, c-a-2]
    elif c-b == 1 and b-a != 1:
        return [1, c-a-2]
    elif b-a >=3 and c-b >=3:
        return [2, c-a-2]
    else:
        return [min((b-a-1), (c-b-1)), c-a-2]


a = eval(input())
b = eval(input())
c = eval(input())
print(numMovesStones(a, b, c))