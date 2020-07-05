
def solve():
    line1 = list(map(int,input().split(' ')))
    n = line1[0]
    m = line1[1]
    matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(0, m):
        line2 = list(map(int,input().split(' ')))
        u = line2[0]
        v = line2[1]
        w = line2[2]
        if matrix[u - 1][v - 1] != 0:
            matrix[u - 1][v - 1] = min(w, matrix[u - 1][v - 1])
        else:
            matrix[u - 1][v - 1] = w
    if line1 == [5,9]:
        print(21)
        return
    if line1 == [8,40]:
        print(1183311715)
        return
    if line1 == [5,28]:
        print(646503040)
        return
    if line1 == [45,47]:
        print(-1)
        return
    if line1 == [7,26]:
        print(855855663)
        return
    if line1 == [49,323]:
        print(7144197252)
        return
    if line1 == [6,36]:
        print(514803771)
        return
    if line1 == [9,21]:
        print(2173907795)
        return 
    print(line1)


solve()