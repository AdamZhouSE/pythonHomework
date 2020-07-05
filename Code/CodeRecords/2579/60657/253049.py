cons=[]
line=int(input())
for i in range(line):
    b=input().split(',')
    b=[int(x) for x in b]
    cons.append(b)
A=int(input())


def maxSideLength( mat, threshold):
    """
    :type mat: List[List[int]]
    :type threshold: int
    :rtype: int
    """
    # the size of mat
    row = len(mat)
    col = len(mat[0])

    # 求解前缀和矩阵P, 输入的矩阵大小是mat的 row 和 col , 但是实际的 返回的P的大小是 row+1  和 col +1
    P = PrefixM(mat, row, col)

    res = 2  # 用来存储子正方形矩阵边长的大小，文中要求的得不明确，我这里设置的是边长至少为2， 也就是这个子矩阵中至少有4个元素
    ans = 0  # 为什么要将ans和res 分开存储，这是因为：如果直接返回 res的话，当没有满足要求的子矩阵的时候，也会返回2，这是不行的
    for c in range(1, col + 1):
        for r in range(1, row + 1):
            # 当起点为（r, c）时， 最大可能的边长为矩阵【（r, c）- (row-1, col-1) 】的较短边
            cmax = min(col + 1 - c, row + 1 - r)
            for n in range(res, cmax + 1):  # 注意这里的边界，实际取值为[res, ..., cmax]
                S = P[r + n - 1][c + n - 1] - P[r - 1][c + n - 1] - P[r + n - 1][c - 1] + P[r - 1][c - 1]
                if S > threshold:
                    break
                if S <= threshold and n >= res:
                    res = n
                    ans = n
    return ans


def PrefixM(mat, row, col):
    # 为矩阵mat 扩展一行、一列
    P = [[0 for i in range(col + 1)] for j in range(row + 1)]
    # 这里从（1，1）开始，是为了当出现r-1= -1 和 c-1= -1 的时候直接为0
    for r in range(1, row + 1):
        for c in range(1, col + 1):
            # 由于起点不同， P矩阵的（r,c）对应的时mat 矩阵[r-1, c-1]:
            P[r][c] = mat[r - 1][c - 1] + P[r - 1][c] + P[r][c - 1] - P[r - 1][c - 1]
    return P

print(maxSideLength(cons,A))