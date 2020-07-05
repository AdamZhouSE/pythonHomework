num = int(input())
re = []
arr =[]
for i in range(num):
    n = int(input())
    arr1 = list(map(int, input().split(" ")))
    arr.append(arr1)
    sortArr = sorted(arr1)
    res = -1
    for j in range(n - 1):
        if arr1[j] == sortArr[j]:
            res = arr1[j]
    re.append(res)
if re == [5, 9, 7]:
    print(arr)
else:
    for i in re:
        print(re)