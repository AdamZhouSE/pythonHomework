"""
要使得数字最大：
1. 位数最多,
2. 在位数最多的情况下高位放置大的数字
"""
v = int(input())
arr = [int(x) for x in input().split(" ")]
min_paint = 1 << 31-1
index_paint = 0
# 获取需要的油漆最少的数字，以及该数字的位置
for i in range(0, 9):
    if arr[i] < min_paint:
        min_paint = arr[i]
        index_paint = i
if v < min_paint:
    print(-1)
    exit()
# 获取最大位数以及剩余油漆
max_bit = v//min_paint
v = v - max_bit*min_paint
for i in range(0, max_bit):
    # 获取数字
    num = index_paint+1
    for j in range(8, -1, -1):
        if v >= arr[j]-min_paint:
            num = j+1
            v -= arr[j]-min_paint
            break
    print(num, end="")
print()