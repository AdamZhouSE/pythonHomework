listN = []
listK = []
n = int(input())
for i in range(n):
    inp = input().split()
    listN.append(int(inp[0]))
    listK.append(int(inp[1]))
for i in range(n):
    N = listN[i]
    K = listK[i]
    print(K**(N-1))