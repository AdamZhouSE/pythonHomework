def test():
    n=int(input())
    mat=[]
    for _ in range(0,n):
        line=input().split(',')
        line=list(map(int,line))
        mat.append(line)
    threshold = int(input())
    max_edge = 0
    for i in range(0, len(mat)):
        for j in range(0, len(mat[0])):
            edge = getEdge(mat, i, j, threshold)
            if edge > max_edge:
                max_edge = edge
    print(max_edge)


def getEdge(mat, x, y, threshold) -> int:
    n = min(len(mat)-x, len(mat[0])-y)
    edge = 0
    for k in range(0, n+1):
        area = 0
        for i in range(x, x + k):
            for j in range(y, y + k):
                    area = mat[i][j] + area
        if area <= threshold:
            edge = k
        else:
            break
    return edge

test()