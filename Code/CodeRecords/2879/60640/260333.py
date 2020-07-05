"""
获取一些点的坐标，
标记第一个点，
对于后面每个点，如果该点与已经标记过的点横纵坐标都不相同，则标记该点
"""
n = int(input())
inp = []
for i in range(n*n):
    inp.append([int(x) for x in input().split(" ")])
mark = [inp[0]]
res = [1]
for i in range(1, n*n):
    x = inp[i][0]
    y = inp[i][1]
    isRepeat = False
    for c in mark:
        if x == c[0] or y == c[1]:
            isRepeat = True
            break
    if not isRepeat:
        mark.append(inp[i])
        res.append(i+1)
for i in range(len(res)-1):
    print(res[i], end=" ")
print(res[len(res)-1])
