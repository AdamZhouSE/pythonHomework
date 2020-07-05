def feasible(matrix, dis):
    for i in range(0, len(matrix)):
        for j in range(i+1, len(matrix)):
            if abs(matrix[i] - matrix[j]) % dis != 0:
                return False
    return True


if __name__ == '__main__':  
    [n, m, d] = list(map(int, input().split(" ")))
    matrix = []
    for i in range(0, n):
        matrix.extend(list(map(int, input().split(" "))))
    if not feasible(matrix, d):
        print(-1)
    else:
        print(len(matrix))
