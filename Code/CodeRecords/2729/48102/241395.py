def single2():
    ls = eval(input())
    left = 0
    right = len(ls) - 1
    while left < right:
        mid = left + (right - left) // 2
        if mid % 2 != 0:
            mid -= 1
        if ls[mid] != ls[mid+1]:
            right = mid
        else:
            left = mid + 2
    return ls[left]


print(single2())