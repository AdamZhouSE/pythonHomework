def treeNums(num):
    if num == 0:
        return 1
    if num == 1:
        return 1
    if num == 2:
        return 2
    res = 0
    for i in range(1, num + 1):
        res = res + treeNums(i - 1) * treeNums(num - i)
    return res


num = int(input())
base = 1e9 + 7
print(int(treeNums(num) % base))