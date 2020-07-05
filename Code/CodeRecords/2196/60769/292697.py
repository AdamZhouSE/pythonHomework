def search(arr, n, m):
    res = []
    for i in range(len(arr) + 1 - n):
        for j in range(len(arr[0]) + 1 - m):
            # print(i, j)
            temp = getSubArr(arr, i, j, n, m)
            if temp not in res:
                res.append(temp)
    # print(res)
    return len(res)


def getSubArr(arr, n, m, n_len, m_len):
    res = ""
    for i in range(n, n + n_len):
        for j in range(m, m + m_len):
            res += arr[i][j]
    return res


n, m = list(map(int, input().split()))
arr = []
for i in range(n):
    arr.append(list(input()))
count = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        # print("--------")
        # print(i, j)
        count += search(arr, i, j)
print(count,end="")