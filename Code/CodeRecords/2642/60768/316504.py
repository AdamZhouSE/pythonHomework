stones = sorted([int(i) for i in input().split(",")])
re = [-1, 0]
a = stones[len(stones) - 2] - stones[0] - 1 - (len(stones) - 3)
b = stones[-1] - stones[1] - 1 - (len(stones) - 3)
re[1] = max(a, b)


def canMove():
    flag = False
    for i in range(len(stones) - 2):
        if not stones[i + 1] == stones[i] + 1:
            break
    else:
        flag = True
    if not flag:
        for i in range(1, len(stones) - 1):
            if not stones[i + 1] == stones[i] + 1:
                break
        else:
            flag = True
    return flag


if canMove():
    if stones[0] < stones[1] - 2 or stones[-1] > stones[len(stones) - 2] + 2:
        re[0] = 2
    else:
        re[0] = 0
else:
    re[0] = re[1]
    for i in range(len(stones)):
        temp = len(stones) - 1
        for j in range(i + 1, len(stones)):
            if stones[j] < stones[i] + len(stones):
                temp -= 1
            else:
                break
        re[0] = min(temp, re[0])

print(re)