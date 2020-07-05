t = int(input())
for i in range(0, t):
    inp = input()
    arr1 = input().split(' ')
    arr2 = input().split(' ')
    res = []
    length = len(arr1) + len(arr2) - 1
    for i in range(0, length):
        res.append(0)
    for i in range(0, len(arr1)):
        for j in range(0, len(arr2)):
            res[i + j] += int(arr1[i]) * int(arr2[j])
    for i in range(0, len(res) - 1):
        print(res[i], end=' ')
    print(res[-1])