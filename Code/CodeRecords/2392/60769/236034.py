num = int(input())
for i in range(num):
    n, k = list(map(int, input().split(" ")))
    arr1 = list(map(int, input().split(" ")))
    res = "No"
    for j in range(1,n):
        if arr1[j]*arr1[j-1]==k:
            res = "Yes"
            break
    print(res)