def treeNums(n):
    if n < 2:
        return 1
    num = [0 for i in range(n + 1)]
    num[0] = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            num[i] = num[i] + num[j - 1] * num[i - j]
    return num[n]


n = int(input())
base = 1e9 + 7
print(int(treeNums(n) % base))