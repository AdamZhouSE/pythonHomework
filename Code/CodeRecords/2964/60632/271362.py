def val(x: str, y: str) -> int:
    a, b = list(x), list(y)
    for i in x:
        if i in y:
            del a[a.index(i)]
            del b[b.index(i)]
    diff = max(len(a), len(b))
    return diff


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
print(*res,end=' ')
