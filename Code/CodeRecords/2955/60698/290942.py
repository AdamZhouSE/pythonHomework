def test():
    strA = input()
    strB = input()
    k = int(input())
    Alen = len(strA)
    Blen = len(strB)
    dist = [[0] * (Blen+1) for _ in range(0, Alen+1)]
    for i in range(1, Alen+1):
        dist[i][0] = dist[i - 1][0] + k
    for i in range(1, Blen+1):
        dist[0][i] = dist[0][i - 1] + k
    for i in range(1, Alen+1):
        for j in range(1, Blen+1):
            temp0 = dist[i - 1][j - 1] + abs(ord(strA[i-1]) - ord(strB[j-1]))
            temp1 = dist[i - 1][j] + k
            temp2 = dist[i][j - 1] + k
            dist[i][j] = min(temp0, temp1)
            dist[i][j] = min(temp2, dist[i][j])
    print( dist[Alen][Blen],end='')


test()