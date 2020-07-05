num = int(input())
for i in range(num):
    n, k = list(map(int, input().split(" ")))
    arr1 = list(map(int, input().split(" ")))
    res = "No"
    for item in arr1:
        arr1.remove(item)
        if k % item == 0 and k / item in arr1:
            res = "Yes"
            break
    print(res)
