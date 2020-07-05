T = int(input())
listN = []
for i in range(T):
    listN.append(int(input()))
    k = listN[i]
    N = 0
    for z in range(k+1):
        N = N+z**5
        print(N)
