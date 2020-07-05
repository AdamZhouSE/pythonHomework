
def func7():
    arr = eval(input())
    target = eval(input())
    left, right = 0, len(arr) - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            ans = mid
            break
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print(ans)


func7()
