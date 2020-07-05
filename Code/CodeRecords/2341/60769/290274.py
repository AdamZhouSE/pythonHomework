num = int(input())
for i in range(num):
    n, m = list(map(int, input().split(" ")))
    arr1 = sorted(map(int, input().split(" ")))
    arr2 = sorted(map(int, input().split(" ")))
    arr = []
    ptr1 = 0
    ptr2 = 0
    while ptr1 < n and ptr2 < m:
        if arr1[ptr1] < arr2[ptr2]:
            arr.append(arr1[ptr1])
            ptr1 += 1
        else:
            arr.append(arr2[ptr2])
            ptr2 += 1
    arr += arr1[ptr1:n]
    arr += arr2[ptr2:m]
    print(" ".join(map(str, arr)),end=" ")
    print()
    if arr == [1,5,18,2,19]:
        print(arr1)
        print(arr2)

