num = int(input())
for i in range(num):
    n = input()
    arr1 = list(map(int, input().split(" ")))
    arr2 = list(map(int, input().split(" ")))
    res = 1
    for item in arr1:
        if item in arr2:
            arr2.remove(item)
        else:
            res = 0
            break
    print(res)