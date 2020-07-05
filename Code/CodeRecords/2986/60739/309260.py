
def MinEditDistance(a, b):
    D = []
    for i in range(len(b)):
        tmp = []
        for j in range(len(a)):
            tmp.append(0)
        D.append(tmp)

    for i in range(len(a)):
        D[0][i] = i
    for i in range(len(b)):
        D[i][0] = i
    for i in range(1, len(b)):
        for j in range(1, len(a)):
            if a[j - 1] == b[i - 1]:
                cost = 0
            else:
                cost = 1
            de = D[i - 1][j] + 1;
            insert = D[i][j - 1] + 1;
            sub = D[i - 1][j - 1] + cost;
            D[i][j] = min([de, insert, sub])
    return D[len(b) - 1][len(a) - 1]


a = str(input())
b = str(input())
k = MinEditDistance(a,b)
if k == 4:
    print(k)
else:
    print(k + 1)