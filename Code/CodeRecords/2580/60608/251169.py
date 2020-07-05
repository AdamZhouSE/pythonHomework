def func26():
    m: int = eval(input())
    n: int = eval(input())
    matrix = [[0 for i in range(0, n)] for j in range(0, m)]
    times = eval(input())
    for time in range(0, times):
        op = eval(input())
        for i in range(0, min(m, op[0])):
            for j in range(0, min(n, op[1])):
                matrix[i][j] += 1
    val = 0
    nums = 0
    for i in range(0, m):
        for j in range(0, n):
            if val < matrix[i][j]:
                val = matrix[i][j]
                nums = 1
            elif val == matrix[i][j]:
                nums += 1
    print(nums)


func26()