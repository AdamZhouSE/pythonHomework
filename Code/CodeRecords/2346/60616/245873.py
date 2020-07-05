import math

testNum=int(input())
for i in range (testNum):
    edges=input().split(' ')
    edge1=int(edges[0])
    edge2 = int(edges[1])
    size=edge1*edge2
    rawInputs=input().split(' ')
    matrix=[]
    for m in range(0,size,edge2):
        tmp=[]
        for n in range(m,m+edge2):
            tmp.append(rawInputs[n])
        matrix.append(tmp)
    left = 0
    top = 0
    bottom = len(matrix) - 1
    right = len(matrix[0]) - 1
    res = []

    while left <= right and top <= bottom:
        # from left to right
        for i in range(left, right + 1):
            res.append(matrix[top][i])
        top += 1
        if top > bottom:
            break

        # from top to bottom
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1
        if left > right:
            break

        # from right to left
        for i in range(right, left - 1, -1):
            res.append(matrix[bottom][i])
        bottom -= 1

        # from bottom to top
        for i in range(bottom, top - 1, -1):
            res.append(matrix[i][left])
        left += 1
    print (" ".join(str(i) for i in res),'')