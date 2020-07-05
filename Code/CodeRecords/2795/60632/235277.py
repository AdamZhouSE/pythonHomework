n = int(input())
array = sorted(list(map(int, input().split(' '))))
# 先求中位数
if n % 2 == 0:
    middle = (array[n // 2] + array[n // 2 - 1]) / 2
else:
    middle = array[n // 2]
if middle % 1 != 0:  # 如果中位数不是整数，则不存在所求非负整数
    print(-1)
else:
    for i in range(n):
        array[i] = abs(array[i] - middle)
    if int(min(array)) == 0 and len(set(array)) <= 2:
        print(int(max(array)))
    else:
        print(-1)