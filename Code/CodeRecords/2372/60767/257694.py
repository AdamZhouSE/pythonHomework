def solution(tip_1, tip_2, x, y, num):
    # 初始化x+1行y+1列的动态规划数组
    init = [[0 for i in range(y + 1)] for j in range(x + 1)]
    # 初始化边界值，即只让一个人收小费
    for m in range(1, y+1):
        init[0][m] = init[0][m - 1] + tip_2[m - 1]
    for n in range(1, x + 1):
        init[n][0] = init[n - 1][0] + tip_1[n - 1]
    # 填充二维数组
    for p in range(1, x + 1):
        for q in range(1, y + 1):
            if p + q <= num:
                init[p][q] = max(init[p][q - 1] + tip_2[p + q - 1], init[p - 1][q] + tip_1[p + q - 1])
            else:
                init[p][q] = max(init[p - 1][q], init[p][q - 1])
    return init[-1][-1]


numOfTests = int(input())
temp = []
for i in range(numOfTests):
    temp = input().split()
    N = int(temp[0])
    X = int(temp[1])
    Y = int(temp[2])
    A = []
    B = []
    temp = input().split()
    for t in temp:
        A.append(int(t))
    temp = input().split()
    for t in temp:
        B.append(int(t))
    print(solution(A,B,X,Y,N))

