num = int(input())
for i in range(num):
    n = int(input())
    arr1 = list(map(int, input().split(" ")))
    sortArr = sorted(arr1)
    res = -1
    for j in range(n-1):
        if arr1[j] == sortArr[j]:
            res = arr1[j]
    print(res)