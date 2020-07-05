num = int(input())
for i in range(num):
    n = int(input())
    arr1 = list(map(int, input().split(" ")))
    temp = arr1[0]
    res = []
    for j in range(1, n):
        res.append(str(temp ^ arr1[j]))
        temp = arr1[j]
    res.append(str(arr1[-1]))
    print(" ".join(res))
