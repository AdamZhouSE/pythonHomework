num = int(input())
for i in range(num):
    n, m, k = list(map(int, input().split(" ")))
    arr1 = sorted(list(map(int, input().split(" "))))
    arr2 = sorted(list(map(int, input().split(" "))))
    ptr1 = 0
    ptr2 = m - 1
    while ptr1 < n and ptr2 >= 0:
        if arr1[ptr1] + arr2[ptr2] == k:
            print(arr1[ptr1], arr2[ptr2])
            ptr1 += 1
            ptr2 -= 1
        elif arr1[ptr1] + arr2[ptr2] < k:
            ptr1 += 1
        else:
            ptr2 -= 1