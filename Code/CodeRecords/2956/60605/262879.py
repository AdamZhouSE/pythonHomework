def mulOfMatrix(matrix1: [[int]], matrix2: [[int]]) -> [[int]]:
    n = len(matrix1)
    newMatrix = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                newMatrix[i][j] += matrix1[i][k] * matrix2[k][j]
    return newMatrix

def quickMul(matrix: [[int]], n: int) -> [[int]]:
    # matrix^n
    binstr = list(str(bin(n))[2:])
    binstr.reverse()
    currentMatrix = None
    tempMatrix = matrix
    for i in binstr:
        if i == "1":
            if currentMatrix == None:
                currentMatrix = tempMatrix
            else:
                currentMatrix = mulOfMatrix(currentMatrix, tempMatrix)
        tempMatrix = mulOfMatrix(tempMatrix, tempMatrix)
    return currentMatrix

def solve() -> int:
    nn = int(input())
    s1 = list(input())
    if nn == 1: return 26
    originMatrix = [[1 for j in range(26)] for i in range(26)]
    for i in range(len(s1)-1):
        a1 = ord(s1[i])-97
        a2 = ord(s1[i+1])-97
        originMatrix[a1][a2] = 0
        originMatrix[a2][a1] = 0
    newMatrix = quickMul(originMatrix, nn-1)
    res = 0
    for i in range(26):
        for j in range(26):
            res += newMatrix[i][j]
    return res


if __name__ == '__main__':
    # print(mulOfMatrix([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    # print(quickMul([[1, 2], [3, 4]], 0))
    print(solve()+1)