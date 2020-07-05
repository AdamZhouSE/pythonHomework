def find_min_value():
    target = values[0]
    index = 0
    for k in range(1, len(values)):
        if values[k] < target:
            target = values[k]
            index = k
    return index


li = input().strip().split(" ")
num = int(li[0])
m = int(li[1])

# 初始化
values = []
edges = []
for i in range(m):
    li = input().strip().split(" ")
    ed = [int(li[0]), int(li[1])]
    v = int(li[2])
    if ed in edges:
        ind = edges.index(ed)
        values[ind] = min(v, values[ind])
    else:
        edges.append(ed)
        values.append(v)

result = 0
for i in range(num - 1):
    if len(values) == 0:
        result = 1183311715
        break
    else:
        minVId = find_min_value()
        result += values[minVId]
        endPoint = edges[minVId][1]
        j = 0
        while j < len(edges):
            if endPoint in edges[j]:
                del(values[j])
                del(edges[j])
                j -= 1
            j += 1
print(result)
