n = int(input())
arr = [-1 for x in range(1000)]


def getMax(num):
    if num == 0:
        return 0
    if arr[num] != -1:
        return arr[num]
    maxNum = max(num, getMax(num // 2) + getMax(num // 3) + getMax(num // 4))
    arr[num] = maxNum
    return arr[num]


for i in range(n):
    print(getMax(int(input())))
