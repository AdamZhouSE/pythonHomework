# 动态规划
def maxMulti(n):
    record = []
    record.append(0)  # 0
    record.append(1)  # 1
    record.append(1)  # 2
    record.append(2)  # 3
    for i in range(4, n + 1):
        temp = 0
        for j in range(1, i // 2 + 1):
            temp = max([temp, max([record[j], j]) * max([record[i - j], i - j])])
        # print("i =", i, "max =", temp)
        record.append(temp)
    return record[n]


a = int(input())
print(maxMulti(a))
