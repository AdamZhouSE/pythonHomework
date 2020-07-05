import math

# values: 价值的数组
# k: k和k之前的可选中
# w: 现在还可以装多重
def dp(values, weights, k, w):
    if w == 0: return 0
    if k == -1: return 0
    if weights[k] > w:
        return dp(values, weights, k-1, w)
    return max(dp(values, weights, k-1, w), values[k] + dp(values, weights, k-1, w-weights[k]))


t = int(input())
liN = []
liArray = []
for i in range(t):
    liN.append(int(input()))
    array = []
    a = input().split(" ")
    for b in a:
        array.append(int(b))
    array = sorted(array)
    liArray.append(array)

for i in range(t):
    n = liN[i]
    array = liArray[i]
    sumArray = sum(array)
    res = dp(array, array, len(array)-1, sumArray//2)
    print(abs(sumArray - res - res))
