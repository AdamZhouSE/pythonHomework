num = int(input())
for i in range(num):
    arr1 = []
    arr2 = []
    n, target = list(map(int, input().split()))
    for j in range(n):
        arr1 += list(map(int, input().split()))
    for j in range(n):
        arr2 += list(map(int, input().split()))
    res = 0
    for item in arr1:
        if target-item in arr2:
            res+=1
    print(res)

