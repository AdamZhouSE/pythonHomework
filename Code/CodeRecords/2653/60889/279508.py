numOfInput = int(input())
for i in range(numOfInput):
    NX = input().split(" ")
    N = int(NX[0])
    X = int(NX[1])
    print((10-X)*(N-1))
    