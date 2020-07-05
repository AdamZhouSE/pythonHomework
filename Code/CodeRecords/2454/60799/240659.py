def search_min_number(aList):
    left, right = 0, len(aList) - 1

    while left <= right:
        mid = int((left + right) / 2)
        if aList[mid] < aList[right]:
            right = mid
        elif aList[mid] > aList[right]:
            left = mid + 1
        else:
            right -= 1
    return aList[left]


print(search_min_number([int(i) for i in input().split(',')]))