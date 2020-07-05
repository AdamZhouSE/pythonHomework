num = int(input())
for j in range(num):
    n = int(input())
    arr1 = list(map(int, input().split(" ")))
    count = 0  # invalid
    res = []
    for i in range(n - 1):
        if arr1[i] == 0:
            count += 1
        elif arr1[i] == arr1[i + 1]:
            res.append(str(2 * arr1[i]))
            arr1[i + 1] = 0
        else:
            res.append(str(arr1[i]))
    res.append(str(arr1[-1]))
    for i in range(count):
        res.append(str(0))
    print(" ".join(res))
