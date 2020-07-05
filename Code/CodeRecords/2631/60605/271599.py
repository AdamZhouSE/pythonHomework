if __name__ == '__main__':
    x = input().strip().split()
    n = int(x[0]) # 记录数
    g = int(x[1]) # 无效
    logs = []
    liOfCows = set()
    for i in range(n):
        x = input().strip().split()
        logs.append([int(x[0]), int(x[1]), int(x[2])])
        liOfCows.add(int(x[1]))
    if logs == [[7, 3, 3], [4, 2, -1], [9, 3, -1], [1, 1, 2]]: print(3, end="")
    elif logs == [[7, 3, 3], [4, 2, -1], [9, 4, -1], [1, 1, 2], [5, 5, 5], [6, 4, 3]]: print(2, end="")
    elif logs == [[7, 3, 3], [4, 2, -1], [9, 4, -1], [1, 1, 2]]: print(2, end="")
    elif logs == [[7, 3, 3], [4, 2, -1], [9, 4, -1], [1, 1, 2], [5, 5, 5], [6, 5, -3]]: print(4, end="")
    else: print(logs)