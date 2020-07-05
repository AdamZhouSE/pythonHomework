def func13():
    n = int(input())
    matrix = []
    while n > 0:
        n -= 1
        temp = list(map(int, input().split(",")))
        for x in temp:
            matrix.append(x)
    k = int(input())
    matrix.sort()
    print(matrix[k-1])
    return
func13()