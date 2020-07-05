# 辅助函数：计算列表中所有区间所覆盖的时间范围
def support(x: list) -> int:
    tmp = []
    for i in x:
        tmp += i
    left, right = min(tmp), max(tmp)
    count = 0
    for i in range(left, right):
        for j in x:
            if i in range(j[0], j[1]):
                count += 1
                break
    return count


n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split(' '))))
result = 0
for i in data:
    tmp = data[:]
    tmp.remove(i)
    if support(tmp) > result:
        result = support(tmp)
print(result)
