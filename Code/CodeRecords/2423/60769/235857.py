num = int(input())
for i in range(num):
    n, k = list(map(int, input().split(" ")))
    arr1 = list(map(int, input().split(" ")))
    arr2 = list(map(int, input().split(" ")))
    res = "Yes"
    for item in arr2:
        if item in arr1:
            arr1.remove(item)
        else:
            res = "No"
            break
    print(res)
            