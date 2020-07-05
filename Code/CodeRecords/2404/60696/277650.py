S = 0
value = []
vectors = []
cnt = 0
paths = []


# 计算路径长度
def len_path(n, s, path):
    global cnt
    path.append(n)
    s += value[n]
    if s == S:
        if path in paths:
            return 
        cnt += 1
        paths.append(path)
        for i in vectors[n]:
            len_path(i, 0, [])  # 如果路径不包含当前结点
    else:
        for i in vectors[n]:
            temp = path.copy()
            temp.append(n)
            len_path(i, s, temp)  # 如果路径包含当前结点
            len_path(i, 0, [])
    return


if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    n = arr[0]
    S = arr[1]
    value = [0 for i in range(n+1)]
    vectors = [[] for i in range(n+1)]
    arr = [int(i) for i in input().split()]
    for i in range(1, n+1):
        value[i] = arr[i-1]
    for i in range(n-1):
        arr = [int(j) for j in input().split()]
        vectors[arr[0]].append(arr[1])
    len_path(1, 0, [])
    print(cnt)