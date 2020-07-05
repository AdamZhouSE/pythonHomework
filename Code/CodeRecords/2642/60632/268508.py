data = list(map(int, input().split(',')))
result = [len(data), 0]
data = sorted(data)
s1 = data[-1] - data[0] + 1 - len(data)  # 范围内未被占的位置个数
s2 = min(data[1] - data[0] - 1, data[-1] - data[-2] - 1)  # 第一次移动时，左右两端损失空间较小的值
result[1] = s1 - s2
for start in range(len(data)):
    i = 0
    while data[start] - data[i] > len(data):
        i += 1
    real_num = start - i + 1
    if real_num == len(data) - 1 and data[start] - data[i] + 1 == len(data) - 1:
        result[0] = min(result[0], 2)
    else:
        result[0] = min(result[0], len(data) - real_num)
print(result)
