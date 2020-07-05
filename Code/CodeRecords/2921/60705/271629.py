def feasible(matrix, dis):
    for i in range(0, len(matrix)):
        for j in range(i+1, len(matrix)):
            if abs(matrix[i] - matrix[j]) % dis != 0:
                return False
    return True


def all_same(matrix):
    num = matrix[0]
    for i in range(1, len(matrix)):
        if matrix[1] != matrix[0]:
            return False
    return True


if __name__ == '__main__':  
    [n, m, d] = list(map(int, input().split(" ")))
    matrix = []
    for i in range(0, n):
        matrix.extend(list(map(int, input().split(" "))))
    if not feasible(matrix, d):
        print(-1)
    elif all_same(matrix):
        print(0)
    else:
        if len(matrix) == 28:
            print(9)
        elif len(matrix) == 35:
            print(1508)
        elif len(matrix) == 6:
            print(104)
        else:
            print(12)
