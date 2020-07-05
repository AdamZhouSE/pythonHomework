def solve(matrix):
    res = matrix.copy()
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            res[i][j] = solve_specific_point(matrix, i, j)
    return res


def solve_specific_point(matrix, i, j):
    if i >= len(matrix) or j >= len(matrix[0]) or i < 0 or j < 0:
        return 10**10
    if matrix[i][j] == 0:
        return 0
    # 不是0，只能是1了
    else:
        if j+1 < len(matrix[0]) and matrix[i][j+1] == 0:
            return 1
        if j > 0 and matrix[i][j-1] == 0:
            return 1
        if i > 0 and matrix[i-1][j] == 0:
            return 1
        if i+1 < len(matrix) and matrix[i+1][j] == 0:
            return 1
        # 这个数字1的周围都没有0
        return 1 + min(solve_specific_point(matrix, i+1, j),
                       solve_specific_point(matrix, i, j+1),
                       solve_specific_point(matrix, i-1, j),
                       solve_specific_point(matrix, i, j-1))

if __name__ == '__main__':
    matrix = []
    line = input()
    while line != "":
        matrix.append(list(map(int, line.split(" "))))
        try:
            line = input()
        except EOFError:
            break
    ans = solve(matrix)
    for i in range(0, len(ans)):
        print(ans[i][0], end="")
        for j in range(1, len(ans[0])):
            print(" "+str(ans[i][j]), end="")
        print()
