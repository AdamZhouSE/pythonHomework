t = int(input())
result = []
for i in range(t):
    n = int(input())
    data = list(map(str, input().split(' ')))
    length = []
    for num in data:  # 统计各数的位数
        length.append(len(num))
    maxi = max(length)
    for j in range(n):  # 将所有数的位数补齐至相同
        data[j] = data[j] + data[j][-1] * (maxi - len(data[j]))
    record = dict(zip(data, length))
    data = sorted(data)
    data.reverse()
    for j in range(n):  # 去除补齐部分，恢复初始数据
        data[j] = data[j][:record[data[j]]]
    result.append(''.join(data))
for i in result:
    print(i)
