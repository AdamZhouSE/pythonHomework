def maxSideLength(mat, threshold) :
    if not mat or not mat[0]: return 0
    row = len(mat)
    col = len(mat[0])
    # 把前i行j列组成的矩形的面积求出来
    prefix = [[0] * (col + 1) for _ in range(row + 1)]

    for i in range(1, row + 1):
        for j in range(1, col + 1):
            prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + mat[i - 1][j - 1]
    left = 0
    right = min(row, col)

    def check(mid):
        for i in range(row - mid + 1):
            for j in range(col - mid + 1):
                if threshold >= prefix[i + mid][j + mid] - prefix[i + mid][j] - prefix[i][j + mid] + \
                        prefix[i][j]:
                    return True
        return False

    while left <= right:
        # print(left, right)
        mid = (left + right) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1

    return right

row=int(input())
mat=[]
for i in range(row):
    mat.append(eval("["+input()+"]"))
print(maxSideLength(mat,int(input())))
