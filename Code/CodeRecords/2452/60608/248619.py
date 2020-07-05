def func17():
    lines: int = eval(input())
    matrix = []
    while lines > 0:
        lines -= 1
        matrix.append(list(eval(input())))
    target = eval(input())
    res = False
    left = 0
    right = len(matrix[0])
    for i in range(0, len(matrix)):
        if matrix[i][right - 1] >= target:
            while left <= right:
                val = (left + right) // 2
                if matrix[i][val] == target:
                    res = True
                    break
                elif matrix[i][val] < target:
                    left = val + 1
                else:
                    right = val - 1
            break
    print(res)


func17()
