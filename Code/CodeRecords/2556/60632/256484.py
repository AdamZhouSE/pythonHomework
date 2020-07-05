# 判断是否重叠，若重叠，返回重叠面积，否则返回0
def support(a: list, b: list, length: int) -> int:
    if abs(a[0] - b[0]) > length or abs(a[1] - b[1]) > length:
        return 0
    else:
        x = length - (abs(a[0] - b[0]))
        y = length - (abs(a[1] - b[1]))
        return x * y


n, k = map(int, input().split(' '))
center = []
for i in range(n):
    center.append(list(map(int, input().split(' '))))
result = []
for i in range(n - 1):
    for j in range(i + 1, n):
        tmp = support(center[i], center[j], k)
        if tmp != 0:
            result.append(tmp)
if len(result) == 0:
    print(0)
elif len(result) > 1:
    print(-1)
else:
    print(*result)
