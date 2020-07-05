num = int(input())
for i in range(num):
    count = int(input())
    arr = input()
    arr = [int(x) for x in arr.split(" ")]
    counts = [0, 0, 0]
    for j in range(count):
        tmp = arr[j] % 3
        counts[tmp] += 1
    maxNum = counts[0]
    minNum = min(counts[1], counts[2])
    maxNum += minNum
    counts[1] -= minNum
    counts[2] -= minNum
    maxNum += counts[1] // 3
    maxNum += counts[2] // 3
    print(maxNum)
