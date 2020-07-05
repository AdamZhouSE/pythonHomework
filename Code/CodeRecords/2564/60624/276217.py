def func3():
    arr = list(map(int, input()[1:-1].split(",")))
    k = int(input())
    x = int(input())
    left = 0
    right = len(arr) - k
    while left < right:
        mid = (left+right) // 2
        if x - arr[mid] > arr[mid+k]-x:
            left = mid+1
        else:
            right = mid
    print(arr[left:left+k])
    return
func3()