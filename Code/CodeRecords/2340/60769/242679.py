num = int(input())
for i in range(num):
    n = int(input())
    arr1 = list(map(int, input().split(" ")))
    maxPos = 0
    maxValue = arr1[0]
    for j in range(n):
        if arr1[j] > maxValue:
            maxValue = arr1[j]
            maxPos = j
    water = 0
    maxHigh = 0
    for j in range(maxPos):
        if arr1[j] > maxHigh:
            maxHigh = arr1[j]
        else:
            water += maxHigh - arr1[j]
    maxHigh = 0
    for j in range(n - 1, maxPos, -1):
        if arr1[j] > maxHigh:
            maxHigh = arr1[j]
        else:
            water += maxHigh - arr1[j]
    print(water)
