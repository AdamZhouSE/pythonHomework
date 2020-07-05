t = int(input())

pow1 = []
pow2 = []
idx1 = []
idx2 = []

for i in range(t):
    a = input().split(" ")
    pow1.append(a[0])
    pow2.append(a[1])
    a = input().split(" ")
    idx1.append(a)
    a = input().split(" ")
    idx2.append(a)

for i in range(t):
    p1 = int(pow1[i])
    p2 = int(pow2[i])
    res = []
    for j in range(p1+p2):
        res.append(0)
    for j in range(p1):
        for k in range(p2):
            res[j+k] += int(idx1[i][j])*int(idx2[i][k])

    while len(res) != 0 and res[len(res) - 1] == 0:
        del res[len(res) - 1]
    for j in range(len(res)):
        print(res[j], end="")
        if j != len(res) - 1:
            print(end=" ")
    print()
