def val(x, y) -> int:
    pass


n = int(input())
data = []
for i in range(n):
    data.append(input())
res = [0 for i in range(8)]
for i in range(len(res)):  # 统计相似度为i+1的字符串对数
    count = 0
    for j in range(n-1):
        for k in range(j+1, n):
            if val(data[j], data[k]) == i+1:
                count += 1
    res[i] = count
for i in data:
    print(i)