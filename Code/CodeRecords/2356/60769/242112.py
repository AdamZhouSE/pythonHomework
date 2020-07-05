num = int(input())
for i in range(num):
    n = int(input())
    arr1 = list(map(int, input().split(" ")))
    left = 1
    right = n - 1
    lmax = arr1[0]
    rmin = arr1[-1]
    while left != right:
        if arr1[left] < lmax or arr1[left] > rmin:
            if arr1[right] > lmax:
                lmax = arr1[left]
            left += 1
        else:
            right -= 1
            if arr1[right] < rmin:
                rmin = arr1[right]
    if lmax <= arr1[left] <= rmin and left != n - 1:
        print(arr1[left])
    else:
        print(-1)
