num = int(input())
inp = input().split()
N, add = int(inp[0]), int(inp[1])
while num >= 0:
    line1 = [[0] * N] * N
    line2 = [[0] * N] * N
    for i in range(0, N):
        line1[i] = input().split(" ")
    for i in range(0, N):
        line2[i] = input().split(" ")
#    print(line1)
#    print(line2)
    count = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for m in range(N):
                    if int(line1[i][j]) + int(line2[k][m]) == add:
                        count += 1
    print(str(count))
    num -= 1